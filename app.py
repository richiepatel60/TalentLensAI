import streamlit as st

from services.parser import extract_text
from services.llm_service import extract_resume_details, generate_summary
from services.matcher import match_resume_to_jd
from services.database import (
    init_db,
    save_resume,
    save_match_result,
)
from ui import (
    load_css,
    render_header,
    render_card,
    end_card,
    render_metric_card,
    render_skill_tags,
    render_status_badge,
    render_page_title,
    render_footer,
    render_info_box,
    render_success_box,
    render_warning_box,
    render_error_box,
    render_divider,
)

# ── Initialize ──
init_db()
load_css()

# ── Sidebar Branding & Navigation ──
render_page_title("TalentLensAI")

page = st.sidebar.radio(
    "Navigation",
    ["📄 Resume Analyzer", "🎯 Resume-JD Matcher"],
    label_visibility="collapsed",
)

# ── Page: Resume Analyzer ──
if page == "📄 Resume Analyzer":
    render_header("📄", "Resume Analyzer", "Upload a resume to extract candidate details and generate an AI summary")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF or DOCX)",
        type=["pdf", "docx"],
        label_visibility="collapsed",
    )

    if uploaded_file:
        text = extract_text(uploaded_file)
        details = extract_resume_details(text)

        if "error" in details:
            st.markdown(render_error_box(f"**Error:** {details['error']}"), unsafe_allow_html=True)
            with st.expander("Raw Response"):
                st.code(details["raw_response"])
        else:
            # Save to DB
            summary = generate_summary(text)
            save_resume(details, summary)

            # Candidate Details
            with render_card("Candidate Details", "👤"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Name**  \n{details['name']}")
                    st.markdown(f"**Email**  \n{details['email']}")
                    st.markdown(f"**Phone**  \n{details['phone']}")
                with col2:
                    st.markdown(f"**Job Title**  \n{details['job_title']}")
                    st.markdown("**Skills**")
                    render_skill_tags(details["skills"], variant="default")
                end_card()

            # AI Summary
            st.markdown(render_divider(), unsafe_allow_html=True)
            with render_card("AI Professional Summary", "🤖"):
                st.markdown(render_info_box(summary), unsafe_allow_html=True)
                end_card()

            st.markdown(render_success_box("✅ Candidate saved to database"), unsafe_allow_html=True)

    render_footer()

# ── Page: Resume-JD Matcher ──
elif page == "🎯 Resume-JD Matcher":
    render_header("🎯", "Resume-JD Matcher", "Compare a resume against a job description and get a match score")

    jd_content = ""
    resume_content = ""

    col1, col2 = st.columns(2)

    # ── Job Description Section ──
    with col1:
        with render_card("Job Description", "📋"):
            jd_input_type = st.radio(
                "JD Input Method",
                ["Upload File", "Paste Text"],
                key="jd_input",
                label_visibility="collapsed",
            )

            if jd_input_type == "Upload File":
                jd_file = st.file_uploader(
                    "Upload JD",
                    type=["pdf", "docx", "txt"],
                    key="jd_file",
                    label_visibility="collapsed",
                )
            else:
                jd_text = st.text_area(
                    "Paste Job Description",
                    height=300,
                    key="jd_text",
                    label_visibility="collapsed",
                )
            end_card()

        if jd_input_type == "Upload File" and jd_file:
            jd_content = extract_text(jd_file)
        elif jd_input_type == "Paste Text":
            jd_content = jd_text

    # ── Resume Section ──
    with col2:
        with render_card("Resume", "📄"):
            resume_input_type = st.radio(
                "Resume Input Method",
                ["Upload File", "Paste Text"],
                key="resume_input",
                label_visibility="collapsed",
            )

            if resume_input_type == "Upload File":
                resume_file = st.file_uploader(
                    "Upload Resume",
                    type=["pdf", "docx"],
                    key="resume_file",
                    label_visibility="collapsed",
                )
            else:
                resume_text = st.text_area(
                    "Paste Resume",
                    height=300,
                    key="resume_text",
                    label_visibility="collapsed",
                )
            end_card()

        if resume_input_type == "Upload File" and resume_file:
            resume_content = extract_text(resume_file)
        elif resume_input_type == "Paste Text":
            resume_content = resume_text

    st.markdown(render_divider(), unsafe_allow_html=True)

    # ── Match Button ──
    if st.button("🎯 Match Candidate", use_container_width=True):
        if not jd_content:
            st.markdown(render_warning_box("⚠️ Please provide a Job Description"), unsafe_allow_html=True)
        elif not resume_content:
            st.markdown(render_warning_box("⚠️ Please provide a Resume"), unsafe_allow_html=True)
        else:
            with st.spinner("Analyzing and matching..."):
                result = match_resume_to_jd(resume_content, jd_content)
                save_match_result(result["match_percentage"], result["recommendation"])

            if "error" in result:
                st.markdown(render_error_box(f"**Error:** {result['error']}"), unsafe_allow_html=True)
                with st.expander("Raw Response"):
                    st.code(result["raw_response"])
            else:
                score = result["match_percentage"]

                # Match Score & Status
                score_col1, score_col2 = st.columns([1, 2])
                with score_col1:
                    render_metric_card(f"{score}%", "Match Score")
                with score_col2:
                    if score >= 90:
                        render_status_badge("excellent", score)
                    elif score >= 70:
                        render_status_badge("good", score)
                    else:
                        render_status_badge("review", score)

                # Matching Skills
                st.markdown(render_divider(), unsafe_allow_html=True)
                with render_card("✅ Matching Skills", "✅"):
                    render_skill_tags(result["matching_skills"], variant="matching")
                    end_card()

                # Missing Skills
                with render_card("❌ Missing Skills", "❌"):
                    render_skill_tags(result["missing_skills"], variant="missing")
                    end_card()

                # Strengths
                with render_card("⭐ Candidate Strengths", "⭐"):
                    render_skill_tags(result["strengths"], variant="default")
                    end_card()

                # Recommendation
                with render_card("📋 Recommendation", "📋"):
                    st.markdown(render_info_box(result["recommendation"]), unsafe_allow_html=True)
                    end_card()

                st.markdown(render_success_box("✅ Matching completed successfully"), unsafe_allow_html=True)

    render_footer()

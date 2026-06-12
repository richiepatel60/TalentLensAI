import streamlit as st

from services.parser import extract_text
from services.llm_service import extract_resume_details, generate_summary
from services.matcher import match_resume_to_jd


from services.database import (
    init_db,
    save_resume,
    save_match_result
)

# Create table if not exists
init_db()
jd_content = ""
resume_content = ""
st.title("TalentLensAI")

page = st.sidebar.radio(
    "Select Feature",
    [
        "Resume Analyzer",
        "Resume-JD Matcher"
    ]
)

if page == "Resume Analyzer":
    
    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    if uploaded_file:

        text = extract_text(uploaded_file)

        details = extract_resume_details(text)

        if "error" in details:

            st.error(details["error"])

            st.text(details["raw_response"])

        else:

            # Save to DB
            summary = generate_summary(text)

            save_resume(details, summary)
            st.subheader("Candidate Details")

            st.write("Name:", details["name"])

            st.write("Email:", details["email"])

            st.write("Phone:", details["phone"])

            st.write("Job Title:", details["job_title"])

            st.write("Skills:")

            for skill in details["skills"]:

                st.write(f"• {skill}")
            st.divider()

            st.subheader("AI Professional Summary")

            st.write(summary)
            st.success("Candidate saved to database")
    
elif page == "Resume-JD Matcher":

    st.title("🎯 Resume-JD Matcher")

    col1, col2 = st.columns(2)

    # Job Description Section
    with col1:
        st.subheader("Job Description")

        jd_input_type = st.radio(
            "JD Input Method",
            ["Upload File", "Paste Text"],
            key="jd_input"
        )

        if jd_input_type == "Upload File":
            jd_file = st.file_uploader(
                "Upload JD",
                type=["pdf", "docx", "txt"],
                key="jd_file"
            )

        else:
            jd_text = st.text_area(
                "Paste Job Description",
                height=300,
                key="jd_text"
            )

    if jd_input_type == "Upload File" and jd_file:
        jd_content = extract_text(jd_file)

    elif jd_input_type == "Paste Text":
        jd_content = jd_text



    # Resume Section
    with col2:
        st.subheader("Resume")

        resume_input_type = st.radio(
            "Resume Input Method",
            ["Upload File", "Paste Text"],
            key="resume_input"
        )

        if resume_input_type == "Upload File":
            resume_file = st.file_uploader(
                "Upload Resume",
                type=["pdf", "docx"],
                key="resume_file"
            )

        else:
            resume_text = st.text_area(
                "Paste Resume",
                height=300,
                key="resume_text"
            )
    if resume_input_type == "Upload File" and resume_file:
        resume_content = extract_text(resume_file)

    elif resume_input_type == "Paste Text":
        resume_content = resume_text

    # if jd_content:
    #     st.subheader("Extracted Job Description")

    #     st.text_area(
    #         "JD Content",
    #         jd_content,
    #         height=200
    #     )

    # if resume_content:

    #     st.subheader("Extracted Resume")

    #     st.text_area(
    #         "Resume Content",
    #         resume_content,
    #         height=200
    #     )
    st.divider()


    if st.button("Match Candidate"):

        if not jd_content:
            st.warning("Please provide Job Description")
        
        elif not resume_content:
            st.warning("Please provide Resume")

        else:

            with st.spinner("Matching Candidate..."):

                result = match_resume_to_jd(
                    resume_content,
                    jd_content
                )
                # st.json(result)
                save_match_result(
                    result["match_percentage"],
                    result["recommendation"]
                )



            if "error" in result:

                st.error(result["error"])

                st.text(result["raw_response"])

            else:

                st.success("Matching Completed")

                st.metric(
                    "Match Percentage",
                    f"{result['match_percentage']}%"
                )
                score = result["match_percentage"]

                if score >= 90:
                    st.success("🟢 Excellent Match")

                elif score >= 70:
                    st.warning("🟡 Good Match")

                else:
                    st.error("🔴 Needs Review")
                st.divider()

                st.subheader("✅ Matching Skills")

                for skill in result["matching_skills"]:
                    st.write(f"• {skill}")

                st.divider()

                st.subheader("❌ Missing Skills")

                for skill in result["missing_skills"]:
                    st.write(f"• {skill}")

                st.divider()

                st.subheader("⭐ Candidate Strengths")

                for strength in result["strengths"]:
                    st.write(f"• {strength}")

                st.divider()

                st.subheader("📋 Recommendation")

                st.info(result["recommendation"])
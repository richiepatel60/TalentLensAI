import streamlit as st

from services.parser import extract_text
from services.llm_service import extract_resume_details

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file:

    text = extract_text(uploaded_file)
    details = extract_resume_details(text)

    st.subheader("Extracted Text")

    st.text_area(
        "",
        text,
        height=400
    )


    st.subheader("Candidate Details")
    
    if "error" in details:

        st.error(details["error"])

        st.text(details["raw_response"])

    else:

        st.write("Name:", details["name"])
        st.write("Email:", details["email"])
        st.write("Phone:", details["phone"])
        st.write("Job Title:", details["job_title"])

        st.write("Skills")

        for skill in details["skills"]:
            st.write(f"• {skill}")

    
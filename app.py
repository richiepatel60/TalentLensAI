import streamlit as st

from services.parser import extract_text
from services.llm_service import extract_resume_details, generate_summary

from services.database import (
    init_db,
    save_resume
)

# Create table if not exists
init_db()

st.title("TalentLensAI")

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
        save_resume(details)
        summary = generate_summary(text)
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
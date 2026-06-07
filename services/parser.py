import fitz
import docx


def extract_text(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):

        text = ""

        pdf = fitz.open(
            stream=uploaded_file.read(),
            filetype="pdf"
        )

        for page in pdf:
            text += page.get_text()

        return text

    elif uploaded_file.name.endswith(".docx"):

        doc = docx.Document(uploaded_file)

        text = "\n".join(
            para.text
            for para in doc.paragraphs
        )

        return text

    return ""
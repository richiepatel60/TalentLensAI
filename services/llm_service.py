import json
import ollama


def extract_resume_details(resume_text):

    prompt = f"""
Analyze the following resume.

Return ONLY valid JSON.

{{
    "name":"",
    "email":"",
    "phone":"",
    "job_title":"",
    "skills":[]
}}

Resume:

{resume_text}
"""

    response = ollama.chat(
        model="gemma4:e4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)

    except Exception as e:
        return {
            "error": str(e),
            "raw_response": content
        }
    
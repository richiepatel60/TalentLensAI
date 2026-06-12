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


def generate_summary(resume_text):

    prompt = f"""
You are an HR assistant.

Analyze the following resume.

Generate a professional summary in 3-5 sentences.

Focus on:
- Experience
- Skills
- Career Focus

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
        ]
    )

    return response["message"]["content"]  


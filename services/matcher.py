import json
import ollama


def match_resume_to_jd(resume_text, jd_text):

    prompt = f"""
    You are an experienced recruiter.

    Compare the candidate resume against the job description.

    Job Description:

    {jd_text}

    Resume:

    {resume_text}

    Return ONLY valid JSON.

    {{
        "match_percentage": 0,
        "matching_skills": [],
        "missing_skills": [],
        "strengths": [],
        "recommendation": ""
    }}
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
            result = json.loads(content)

            matching_skills = result.get(
                "matching_skills",
                []
            )

            missing_skills = result.get(
                "missing_skills",
                []
            )

            total_required = (
                len(matching_skills)
                + len(missing_skills)
            )

            if total_required > 0:

                calculated_score = round(
                    (
                        len(matching_skills)
                        / total_required
                    ) * 100
                )

            else:
                calculated_score = 0

            result["match_percentage"] = calculated_score

            return result

    except Exception as e:

            return {
                "error": str(e),
                "raw_response": content
            }
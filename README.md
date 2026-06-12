# TalentLensAI

TalentLensAI is an AI-powered resume analysis and candidate matching platform built using Python, Streamlit, Ollama, Gemma, and SQLite.

The application helps automate resume screening by extracting structured candidate information, generating AI-powered professional summaries, and matching candidate resumes against job descriptions using a local Large Language Model (LLM).

All AI processing runs locally using Ollama and Gemma, eliminating the need for external API keys while maintaining data privacy.

---

## Features

### Resume Analyzer

Upload resumes in PDF or DOCX format and automatically extract:

* Name
* Email
* Phone Number
* Job Title
* Skills

### AI Professional Summary

Generate concise professional summaries highlighting:

* Experience
* Technical skills
* Career focus

### Resume-JD Matcher

Compare a candidate resume against a job description and generate:

* Match Percentage
* Matching Skills
* Missing Skills
* Candidate Strengths
* Hiring Recommendation

### Deterministic Skill-Based Scoring

Instead of relying entirely on the LLM for scoring:

* Gemma extracts matching and missing skills
* Python calculates the final match percentage

This improves consistency and reduces dependence on model-generated numerical values.

### Local AI Processing

* Runs completely on your machine
* Powered by Ollama and Gemma
* No external API keys required
* Privacy-friendly architecture

### Database Storage

Stores:

* Candidate information
* AI-generated summaries
* Resume-JD match results

using SQLite.

---

## Architecture

### Resume Analyzer Flow

```text
Resume Upload
      |
      v
PDF/DOCX Extraction
      |
      v
Gemma (Ollama)
      |
      +----------------+
      |                |
      v                v
Candidate Details   AI Summary
      |                |
      +-------+--------+
              |
              v
           SQLite
              |
              v
        Streamlit UI
```

### Resume-JD Matcher Flow

```text
Resume + Job Description
            |
            v
      Gemma (Ollama)
            |
            +------------------+
            |                  |
            v                  v
    Matching Skills      Missing Skills
            |
            v
   Python Score Engine
            |
            v
      Match Percentage
            |
            v
      Recommendation
            |
            v
          SQLite
```

---

## Tech Stack

### Frontend

* Streamlit

### Document Processing

* PyMuPDF
* python-docx

### AI Layer

* Ollama
* Gemma

### Database

* SQLite

### Language

* Python

---

## Project Structure

```text
TalentLensAI/
│
├── app.py
│
├── services/
│   ├── parser.py
│   ├── llm_service.py
│   ├── matcher.py
│   └── database.py
│
├── database/
│   └── resumes.db
│
├── uploads/
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd TalentLensAI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com

Pull the Gemma model:

```bash
ollama pull gemma4:e4b
```

Verify installation:

```bash
ollama list
```

---

## Run Application

Start Ollama:

```bash
ollama serve
```

Run Streamlit:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Current Capabilities

* Resume upload and parsing
* Candidate information extraction
* AI-generated professional summaries
* Resume-JD matching
* Deterministic skill-based scoring
* Local LLM execution
* SQLite persistence
* Match result storage

---

## Future Enhancements

* Candidate Dashboard
* Resume Ranking
* Resume Search
* Vector Database Integration
* Semantic Candidate Search
* RAG-Based Candidate Discovery
* Multi-user Support
* Recruiter Analytics Dashboard

---

## Learning Outcomes

This project demonstrates:

* Python application development
* Streamlit UI development
* Local LLM integration with Ollama
* Prompt engineering
* JSON-based structured extraction
* SQLite database operations
* Resume analysis automation
* AI-powered candidate matching
* Deterministic scoring design
* End-to-end AI application development

---


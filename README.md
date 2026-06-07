# TalentLensAI

TalentLensAI is an AI-powered resume analysis platform built using Streamlit, Ollama, Gemma, and SQLite.

The application allows users to upload resumes in PDF or DOCX format, automatically extracts candidate information using a local Large Language Model (LLM), generates a professional summary, and stores the results in a SQLite database.

## Features

### Resume Upload

* Upload PDF resumes
* Upload DOCX resumes

### AI Resume Parsing

Extracts candidate information using a local Gemma model through Ollama:

* Name
* Email
* Phone Number
* Job Title
* Skills

### AI Professional Summary

Generates a concise professional summary highlighting:

* Experience
* Technical skills
* Career focus

### Local AI Processing

* Runs entirely on your machine
* Uses Ollama for local inference
* No external API keys required

### Database Storage

Stores extracted candidate information and AI-generated summaries using SQLite.

---

## Architecture

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

Activate:

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Install Ollama from:

https://ollama.com

Pull the Gemma model:

```bash
ollama pull gemma4:e4b
```

Verify:

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
* Local LLM execution
* SQLite persistence

---

## Future Enhancements

* Job Description Matching
* Resume Ranking
* Candidate Dashboard
* Resume Search
* Vector Database Integration
* RAG-Based Candidate Discovery

---

## Learning Outcomes

This project demonstrates:

* Python application development
* Streamlit UI development
* Local LLM integration with Ollama
* Prompt engineering
* JSON-based structured extraction
* SQLite database operations
* AI-powered document analysis

---

## License

This project is intended for learning, experimentation, and portfolio purposes.

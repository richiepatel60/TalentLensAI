import sqlite3

DB_PATH = "database/resumes.db"


def init_db():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,
        email TEXT,
        phone TEXT,
        job_title TEXT,

        skills TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_resume(details):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    skills = ",".join(details["skills"])

    cursor.execute("""
    INSERT INTO resumes
    (
        name,
        email,
        phone,
        job_title,
        skills
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        details["name"],
        details["email"],
        details["phone"],
        details["job_title"],
        skills
    ))

    conn.commit()
    conn.close()


def get_all_resumes():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM resumes")

    rows = cursor.fetchall()

    conn.close()

    return rows
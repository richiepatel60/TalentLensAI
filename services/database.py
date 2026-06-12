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

            summary TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jd_matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_percentage INTEGER,
            recommendation TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_resume(details,summary):

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
            skills,
            summary
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            details["name"],
            details["email"],
            details["phone"],
            details["job_title"],
            skills,
            summary
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

def save_match_result(
    match_percentage,
    recommendation):

    conn = sqlite3.connect(
        "database/resumes.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO jd_matches
        (
            match_percentage,
            recommendation
        )
        VALUES (?, ?)
        """,
        (
            match_percentage,
            recommendation
        )
    )

    conn.commit()
    conn.close()
import sqlite3
from datetime import datetime


DATABASE = "resume_analyzer.db"


def get_db():

    connection = sqlite3.connect(
        DATABASE
    )

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():

    connection = get_db()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS analyses (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            resume_name TEXT,

            final_score REAL,

            skill_score REAL,

            similarity_score REAL,

            ats_score REAL,

            keyword_coverage REAL,

            matched_skills TEXT,

            missing_skills TEXT,

            matched_keywords TEXT,

            missing_keywords TEXT,

            created_at TEXT

        )
        """
    )

    connection.commit()

    connection.close()


def save_analysis(data):

    connection = get_db()

    connection.execute(
        """
        INSERT INTO analyses (

            resume_name,
            final_score,
            skill_score,
            similarity_score,
            ats_score,
            keyword_coverage,
            matched_skills,
            missing_skills,
            matched_keywords,
            missing_keywords,
            created_at

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,

        (

            data["resume_name"],

            data["final_score"],

            data["skill_score"],

            data["similarity_score"],

            data["ats_score"],

            data["keyword_coverage"],

            ", ".join(
                data["matched_skills"]
            ),

            ", ".join(
                data["missing_skills"]
            ),

            ", ".join(
                data["matched_keywords"]
            ),

            ", ".join(
                data["missing_keywords"]
            ),

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
    )

    connection.commit()

    connection.close()


def get_all_analyses():

    connection = get_db()

    analyses = connection.execute(
        """
        SELECT *
        FROM analyses
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return analyses


def get_analysis(analysis_id):

    connection = get_db()

    analysis = connection.execute(
        """
        SELECT *
        FROM analyses
        WHERE id = ?
        """,
        (analysis_id,)
    ).fetchone()

    connection.close()

    return analysis
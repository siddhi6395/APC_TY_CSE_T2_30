"""
database.py - SQLite History Database Management Module
Demonstrates SQLite integration, parameterized SQL statements, and JSON serialization.
(SYLLABUS CONCEPT: Unit 2 - File & Database Operations)
"""

import sqlite3
import json
import os
from datetime import datetime

DB_NAME = "resume_analyzer_history.db"


def get_connection(db_path: str = DB_NAME):
    """
    Establishes and returns a SQLite database connection with row factory.
    (SYLLABUS CONCEPT: Unit 2 - Database Connection)
    """
    db_path_str = str(db_path)
    if db_path_str != ':memory:' and not db_path_str.startswith('file:'):
        db_dir = os.path.dirname(os.path.abspath(db_path_str))
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)
    conn = sqlite3.connect(db_path_str)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str = DB_NAME):
    """
    Initializes SQLite database schema on application first launch.
    (SYLLABUS CONCEPT: Unit 2 - SQLite DDL)
    """
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            analysis_date TEXT NOT NULL,
            overall_score REAL NOT NULL,
            grade TEXT NOT NULL,
            career_field TEXT NOT NULL,
            word_count INTEGER NOT NULL,
            char_count INTEGER NOT NULL,
            skills_count INTEGER NOT NULL,
            sections_json TEXT NOT NULL,
            skills_json TEXT NOT NULL,
            contact_json TEXT NOT NULL,
            breakdown_json TEXT NOT NULL,
            strengths_json TEXT NOT NULL,
            suggestions_json TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_analysis_record(record_data: dict, db_path: str = DB_NAME) -> int:
    """
    Saves a completed analysis record to SQLite database using parameterized SQL queries.
    (SYLLABUS CONCEPT: Unit 2 - SQLite DML & JSON Handling)
    """
    conn = get_connection(db_path)
    cursor = conn.cursor()
    
    filename = record_data.get("filename", "Unknown.pdf")
    analysis_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    overall_score = float(record_data.get("overall_score", 0.0))
    grade = record_data.get("grade", "N/A")
    career_field = record_data.get("career_field", "Undetermined")
    word_count = int(record_data.get("word_count", 0))
    char_count = int(record_data.get("char_count", 0))
    skills_count = int(record_data.get("skills_count", 0))
    
    # Serialize Python dictionaries and lists to JSON strings
    sections_json = json.dumps(record_data.get("sections", {}))
    skills_json = json.dumps(record_data.get("skills_by_category", {}))
    contact_json = json.dumps(record_data.get("contact", {}))
    breakdown_json = json.dumps(record_data.get("breakdown", {}))
    strengths_json = json.dumps(record_data.get("strengths", []))
    suggestions_json = json.dumps(record_data.get("suggestions", []))
    
    cursor.execute("""
        INSERT INTO history (
            filename, analysis_date, overall_score, grade, career_field,
            word_count, char_count, skills_count, sections_json,
            skills_json, contact_json, breakdown_json, strengths_json, suggestions_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        filename, analysis_date, overall_score, grade, career_field,
        word_count, char_count, skills_count, sections_json,
        skills_json, contact_json, breakdown_json, strengths_json, suggestions_json
    ))
    
    record_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return record_id


def fetch_all_history(db_path: str = DB_NAME) -> list:
    """
    Fetches list of all saved analysis history records ordered by newest first.
    (SYLLABUS CONCEPT: Unit 2 - Database Selection)
    """
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, filename, analysis_date, overall_score, grade, career_field, word_count, skills_count
        FROM history
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def fetch_record_by_id(record_id: int, db_path: str = DB_NAME) -> dict:
    """
    Fetches a single full analysis record by primary key ID and deserializes JSON fields.
    (SYLLABUS CONCEPT: Unit 2 - Database Querying & JSON Deserialization)
    """
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE id = ?", (record_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    
    res = dict(row)
    res["sections"] = json.loads(res["sections_json"])
    res["skills_by_category"] = json.loads(res["skills_json"])
    res["contact"] = json.loads(res["contact_json"])
    res["breakdown"] = json.loads(res["breakdown_json"])
    res["strengths"] = json.loads(res["strengths_json"])
    res["suggestions"] = json.loads(res["suggestions_json"])
    return res


def delete_record_by_id(record_id: int, db_path: str = DB_NAME):
    """Deletes a single analysis record from SQLite database."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()


def clear_all_history(db_path: str = DB_NAME):
    """Clears all records from the history table."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history")
    conn.commit()
    conn.close()

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jobradar.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vacancies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            salary_min REAL,
            salary_max REAL,
            created_at TEXT,
            UNIQUE(title, company, location)
        )
    """)
    conn.commit()
    conn.close()

def save_vacancy(title, company, location, salary_min, salary_max):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO vacancies (title, company, location, salary_min, salary_max, created_at)
            VALUES (?, ?, ?, ?, ?, datetime('now'))
        """, (title, company, location, salary_min, salary_max))
        conn.commit()
        saved = True
    except sqlite3.IntegrityError:
        saved = False
    finally:
        conn.close()
    return saved
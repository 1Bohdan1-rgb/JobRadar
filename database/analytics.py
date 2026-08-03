import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jobradar.db")

def get_all_vacancies():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vacancies")
    rows = cursor.fetchall()
    conn.close()
    return rows

def average_salary():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT AVG(salary_min), AVG(salary_max)
        FROM vacancies
        WHERE salary_min > 0 AND salary_max > 0
    """)
    result = cursor.fetchone()
    conn.close()
    return result

def top_companies(limit=5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT company, COUNT(*) as count
        FROM vacancies
        GROUP BY company
        ORDER BY count DESC
        LIMIT ?
    """, (limit,))
    results = cursor.fetchall()
    conn.close()
    return results

def missing_salary_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*) FROM vacancies
        WHERE salary_min = 0 OR salary_min IS NULL
    """)
    result = cursor.fetchone()
    conn.close()
    return result[0]

def total_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM vacancies")
    result = cursor.fetchone()
    conn.close()
    return result[0]
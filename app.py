from flask import Flask, render_template, redirect, url_for
from database.analytics import average_salary, top_companies, missing_salary_count, total_count, get_all_vacancies
from database.db import init_db
import subprocess
import sys
import os

app = Flask(__name__)
init_db()

@app.route("/")
def dashboard():
    total = total_count()
    avg_min, avg_max = average_salary()
    missing = missing_salary_count()
    companies = top_companies()
    vacancies = get_all_vacancies()

    return render_template(
        "dashboard.html",
        total=total,
        avg_min=avg_min or 0,
        avg_max=avg_max or 0,
        missing=missing,
        companies=companies,
        vacancies=vacancies
    )

@app.route("/refresh", methods=["POST"])
def refresh():
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scraper", "fetch_jobs.py")
    subprocess.run([sys.executable, script_path])
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
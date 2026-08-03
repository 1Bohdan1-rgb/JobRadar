import os
import sys
import requests
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.db import init_db, save_vacancy

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"

search_terms = ["python developer", "junior developer", "IT support"]

init_db()

for term in search_terms:
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 20,
        "what": term,
        "where": "London"
    }

    response = requests.get(url, params=params)
    print(f"Status: {response.status_code}, Response: {response.text[:200]}")
    data = response.json()

    print(f"\n=== Searching: {term} ({data.get('count', 0)} total found) ===")

    for job in data.get("results", []):
        title = job.get("title")
        company = job.get("company", {}).get("display_name")
        location = job.get("location", {}).get("display_name")
        salary_min = job.get("salary_min")
        salary_max = job.get("salary_max")

        is_new = save_vacancy(title, company, location, salary_min, salary_max)
        if is_new:
            print(f"Saved: {title} at {company}")
        else:
            print(f"Skipped (duplicate): {title} at {company}")

print("\nDone!")
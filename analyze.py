from database.analytics import average_salary, top_companies, missing_salary_count, total_count

print("=== JobRadar Analytics ===\n")

total = total_count()
print(f"Total vacancies: {total}")

avg_min, avg_max = average_salary()
print(f"Average salary min: £{avg_min:,.2f}" if avg_min else "Average salary min: N/A")
print(f"Average salary max: £{avg_max:,.2f}" if avg_max else "Average salary max: N/A")

missing = missing_salary_count()
print(f"Vacancies without salary info: {missing}")

print("\n=== Top 5 companies by vacancy count ===")
for company, count in top_companies():
    print(f"{company}: {count} vacancies")
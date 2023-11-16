companies = {}

while True:
    input_line = input()
    if input_line == "End":
        break

    company_name, employee_id = input_line.split(" -> ")

    if company_name not in companies:
        companies[company_name] = set()
    companies[company_name].add(employee_id)

# Print the company name and each employee's id
for company_name, employee_ids in companies.items():
    print(company_name)
    for employee_id in employee_ids:
        print(f"-- {employee_id}")

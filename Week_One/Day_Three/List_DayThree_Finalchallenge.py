employee_names = ["Bhargav", "Rahul", "Anu", "Priya", "Kiran"]

salaries = [95000, 75000, 120000, 85000, 110000]

skills = ["Python", "SQL", "Pandas", "FastAPI"]


def sort_salaries(salary_values):
    ascending = sorted(salary_values)
    descending = sorted(salary_values, reverse=True)

    return ascending, descending


if __name__ == "__main__":
    ascending_order, descending_order = sort_salaries(salaries)

    print(f"First employee: {employee_names[0]}")
    print(f"Last employee: {employee_names[-1]}")
    print(f"Total employees: {len(employee_names)}")
    print(f"First two employees: {employee_names[:2]}")
    print(f"Lowest Salary: {min(salaries)}")
    print(f"Highest Salary: {max(salaries)}")
    print(f"Total Salary: {sum(salaries)}")
    print(f"Average Salary: {sum(salaries) / len(salaries)}")
    print(f"Original salaries: {salaries}")
    print(f"Ascending salaries: {ascending_order}")
    print(f"Descending salaries: {descending_order}")
    print(f"Skills: {skills}")
employee = "Bhargav,AI Engineering,7,95000.50"
filename = "employee_data.csv"
skills = "Python SQL Pandas Python FastAPI"

data = employee.split(",")


data[2] = int(data[2])
data[3] = float(data[3])


print(f"Employee: {data[0]}")
print(f"Department: {data[1]}")
print(f"Experience: {data[2]} years")
print(f"Salary: {data[3]}")
print(f"Experience next year: {data[2] + 1} years")
print(f"Salary after increase: {data[3] + 5000}")
print(f"Python skill count: {skills.count('Python')}")
print(f"CSV file: {filename.endswith('.csv')}")
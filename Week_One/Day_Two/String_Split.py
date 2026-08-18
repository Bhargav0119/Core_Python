# skills = "Python,SQL,Pandas,FastAPI"

# result = skills.split(",")

# print(result)

# print(type(result))

employee = "Bhargav,AI Engineering,7,95000"

data = employee.split(",")

print(data)
print(type(data))
print(data[0])
print(data[1])
print(data[2])
print(data[3])

data[2] = int(data[2])
data[3] = int(data[3])

# print(type(data[2]))
# print(type(data[3]))

experience_next_year = data[2] + 1
salary_after_increase = data[3] + 5000

# print("Experience next year:" + str(experience_next_year))
# print("Salary after increase:" + str(salary_after_increase))
print(f"Experience next year: {experience_next_year}")
print(f"Salary after increase: {salary_after_increase}")
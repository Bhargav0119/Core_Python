agents = ["Policy Agent", "Payroll Agent", "Employee Agent"]

user_request = "payroll"


for agent in agents:
    if agent == "Payroll Agent" and user_request == "payroll":
        print("Payroll Agent selected")
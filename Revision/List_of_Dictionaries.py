agents = [
    {"name": "Policy Agent", "status": "Active"},
    {"name": "Payroll Agent", "status": "Inactive"},
    {"name": "Leave Agent", "status": "Active"}
]

for agent in agents:
    # print("Agent Name : " + agent["name"])
    if agent["status"] == "Active":
        print(agent["name"] + " is active")
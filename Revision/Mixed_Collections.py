agents = [
    {
        "name": "Policy Agent",
        "status": "Active",
        "tools": ["FastAPI", "SQL"]
    },
    {
        "name": "Payroll Agent",
        "status": "Inactive",
        "tools": ["Python"]
    },
    {
        "name": "Leave Agent",
        "status": "Active",
        "tools": ["FastAPI", "Vertex AI"]
    }
]

for agent in agents:
    if agent["status"] == "Active":
        print(agent["name"])
        for tool in agent["tools"]:
            print("Tool :" + tool)
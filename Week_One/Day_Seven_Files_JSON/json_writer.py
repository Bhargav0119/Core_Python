import json

agent = {
    "name": "Payroll Agent",
    "status": "Active",
    "model": "Gemini",
    "tools": ["Python", "FastAPI"]
}

with open("payroll_agent.json", "w") as json_file:
    json.dump(agent, json_file, indent=4)
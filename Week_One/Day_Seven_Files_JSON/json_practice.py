import json

# {
#     "name": "Payroll Agent",
#     "status": "Active",
#     "model": "Gemini",
#     "tools": ["Python", "FastAPI"]
# }

with open("payroll_agent.json" , "r") as json_file:
    agent_data = json.load(json_file)

print("Agent Name: " + agent_data["name"])
print("Status: " + agent_data["status"])
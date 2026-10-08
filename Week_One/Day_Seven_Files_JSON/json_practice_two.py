import json

new_agent = {
    "name": "Leave Agent",
    "status": "Active",
    "model": "Gemini"
}

with open("leave_agent.json", "w") as json_file:
    json.dump(new_agent, json_file, indent=4)
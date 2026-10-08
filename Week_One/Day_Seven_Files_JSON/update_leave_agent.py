import json

with open("leave_agent.json", "r") as file:
   new_agent  = json.load(file)

new_agent["status"] = "Inactive"

print("status:" + new_agent["status"])

with open("leave_agent.json", "w") as file:
   json.dump(new_agent, file, indent=4)
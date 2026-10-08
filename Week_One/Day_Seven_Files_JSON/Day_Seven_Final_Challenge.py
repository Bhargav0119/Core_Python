import json

with open("policy_agent.json", "r") as file:
   current_file = json.load(file)

   current_file["status"] = "Inactive"
   current_file["model"] = "Gemini"

with open("updated_policy_agent.json", "w") as file:
   json.dump(current_file, file, indent=4)
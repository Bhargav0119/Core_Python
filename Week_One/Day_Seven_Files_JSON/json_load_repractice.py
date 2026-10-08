import json

with open("policy_agent.json", "r") as file:
    modified_file = json.load(file)

print("Agent Name: " + modified_file["name"])
print("Status: " + modified_file["status"]) 
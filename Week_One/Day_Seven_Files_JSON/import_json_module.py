import json

with open("leave_agent.json", "r") as json_file:
  absorb_mode  = json.load(json_file)
print("Agent Name: " + absorb_mode["name"])
print("Model: " + absorb_mode["model"])
print("Status: " + absorb_mode["status"])

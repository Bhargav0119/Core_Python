import json

agent = {
    "name" : "Policy Agent",
    "status" : "Active",
}

with open("policy_agent.json", "w") as saved_file:
    json.dump(agent, saved_file , indent =4)
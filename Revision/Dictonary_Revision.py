agent = {
"name"  : "Policy Agent",
"status" : "Active",
"tool"   : "FastAPI",
"request" : 100,
"production" : True
}

# print(agent["name"])
# print(agent["status"])
# print(agent["tool"])

# agent["status"] = "Inactive"
# print(agent)

# agent["environment"] = "Prod"
# print(agent)

# print(agent["model"])

# print(agent.get("model", "Model not found"))

for key, value in agent.items():
    print(key + " : " + str(value))
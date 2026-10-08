import json

with open("agent_config.json", "r") as json_file:
         dict_stored = json.load(json_file)
# print(dict_stored)
print("Agent Name: " + dict_stored["name"])
print("Model: " + dict_stored["model"])
for tool in dict_stored["tools"]:
    print("Tool: " + tool)

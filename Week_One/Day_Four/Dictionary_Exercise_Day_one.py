from pprint import pprint


agent = {
    "name": "PolicyAgent",
    "framework": "Google ADK",
    "model": "Gemini",
    "active": True,
    "tools": ["Policy API", "Employee API"],
}

print(agent)

# print("Agent: " + agent["name"])
# print("Framework: " + agent["framework"])
# print("Active: " + str(agent["active"]))
# print("First Tool: " + agent["tools"][0])
# print("Last Tool: " + agent["tools"][-1])
# print("Model: " + agent["model"])

agent["active"] = False
agent["environment"] = "Vertex AI"
agent["tools"].append("MCP Server")


pprint(agent)



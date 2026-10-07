agent = {
    "name": "Policy Agent",
    "tools": ["FastAPI", "SQL", "Vertex AI"]
}

# for key, value in agent.items():
print("Agent: " +agent["name"])
for tool in agent["tools"]:
    print("Tool: " + tool)

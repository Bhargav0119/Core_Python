agent_response = {
    "agent": "PolicyAgent",
    "status": "success"
}

# print(agent_response.get("key", "default value"))
# print(agent_response.get["error"])
print(agent_response.get("error"))
print(agent_response.get("error", "No error found"))
print(agent_response.get("status", "No status found"))
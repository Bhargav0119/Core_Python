agent_response = {
    "agent": "PolicyAgent",
    "status": "success",
    "metrics": {
        "latency_ms": 450,
        "input_tokens": 120,
        "output_tokens": 80
    },

    "tools_used": ["Policy API", "MCP Server"]

}



print(agent_response["metrics"]["latency_ms"])
print("Agent : " + agent_response["agent"])
print("Status : " + agent_response["status"])
print("Latency :" + str(agent_response["metrics"]["latency_ms"]) + " ms")
print("Input Tokens :" + str(agent_response["metrics"]["input_tokens"]) + " tokens")
print("Output Tokens :" + str(agent_response["metrics"]["output_tokens"]) + " tokens")
print("First tool used : " + agent_response["tools_used"][0])
print("Last tool used : " + agent_response["tools_used"] [-1])

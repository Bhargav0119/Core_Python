from pprint import pprint

ai_agent = {
    "name": "EmployeeAgent",
    "active": True,
    "tools": ["Employee API", "Policy API"],
    "metrics": {
        "latency_ms": 320,
        "input_tokens": 150
    },
    "environments": ("dev", "test", "prod")
}

print("Agent: " + ai_agent["name"]) 
print("Latency: " + str(ai_agent["metrics"]["latency_ms"]) + " ms")
print("Production environment: " + ai_agent["environments"][-1])

ai_agent["active"] = False
ai_agent["tools"].append("MCP Server")
ai_agent["framework"] = "Google ADK"

pprint(ai_agent)
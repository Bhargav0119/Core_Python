agent = {
    "name": "Policy Agent",
    "config": {
        "model": "Gemini",
        "environment": "PROD"
    }
}

print("Agent :" + agent["name"])
print("Model :" + agent["config"]["model"])
print("Environment :" + agent["config"]["environment"])
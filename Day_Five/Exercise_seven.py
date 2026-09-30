agent_active = True
latency_ms = 650

if agent_active == True and latency_ms < 500:
    print("Agent can process the request")
else:
    print("Agent cannot process the request")
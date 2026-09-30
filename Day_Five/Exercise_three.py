agent_status = "error"

if agent_status == "active":
    print("Policy agent is ready")
elif agent_status == "maintenance":
    print("Policy agent is in maintenance mode")
else:
    print("Policy agent is in unknown state")
try:
    with open("missing_agent_info.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Agent file not found")

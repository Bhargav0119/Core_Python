# file = open("agent_info.txt", "r")
# content = file.read()
# print(content)
# file.close()

# with open("agent_info.txt", "r") as file:
#     content = file.read()
#     print(content)

with open("agent_info.txt", "r") as file:
    for line in file:
        print(line.strip())
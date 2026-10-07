# tools = {"FastAPI", "Docker", "FastAPI", "Git", "Docker"}
# # print(tools)

# tools.add("Jenkins")
# # print(tools)

# tools.remove("Docker")
# # tools.remove("Docker")
# tools.discard("Docker")
# # print(tools)

# # for tool in tools:
# #     if tool == "Jenkins":
# #         print("jenkins is available")
# #     else:
# #         print("Jenkins is not available")

# if "Jenkins" in tools:
#     print("Jenkins is available") 
# else:
#     print("jenkins is not available")

tools = {"FastAPI", "Docker", "Git"}

tools.add("Jenkins")
tools.add("Docker")
tools.discard("Git")

if "Jenkins" in tools:
    print("jenkins tool found")
else:
    print("jenkins tool not found")

print(tools)
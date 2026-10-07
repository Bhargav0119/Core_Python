# environments = ("DEV", "TEST", "PROD")

# print("First Environment: " + environments[0])
# print("Last Environment: " + environments[-1])

# environments[1] = "UAT"


#------Slicing Tuples----------------#
environments = ("DEV", "TEST", "UAT", "STAGING", "PROD")
# print(environments[1:4])
# for env in environments:
#     print("Environment: " + env)
for env in environments:
    if env ==  "PROD":
        print("Production environment found")
    else:
        print("Non-Production: " + env)



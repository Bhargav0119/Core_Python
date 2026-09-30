latency_ms = 350
has_error = True

if latency_ms > 500 or has_error == True:
    print("Escalate request")
else:
    print("Do not escalate request")
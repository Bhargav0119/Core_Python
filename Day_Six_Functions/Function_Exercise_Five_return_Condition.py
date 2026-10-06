def check_latency(latency_ms):

    if latency_ms > 500:
        return "High Latency"
    else:
        return "Normal Latency"

result = check_latency(650)
print(result)
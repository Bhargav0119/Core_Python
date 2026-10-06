def check_latency(latency_ms):

    if latency_ms >500:
        return "High Latency"
    elif latency_ms > 300:
        return "Moderate Latency"
    else:
        return "Normal Latency"

result = check_latency(450)
print("Latency status : " + result)

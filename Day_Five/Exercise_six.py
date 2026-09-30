latency_ms = 450

if latency_ms > 500:
    print("High Latency")
elif latency_ms > 300:
    print("Moderate Latency")
else:
    print("Low Latency")
def calculate_latency(processing_time, network_time):
    total_latency = processing_time + network_time
    return total_latency

result = calculate_latency(300, 100)
print(result)
def calculate_average_latency(total_latency, number_of_requests):
    try:
        calculate_average = total_latency / number_of_requests
        return calculate_average
    except ZeroDivisionError:
        return "Unable to calculate average latency due to zero requests."

result = calculate_average_latency(1000, 0)
print(result)
print(type(result))
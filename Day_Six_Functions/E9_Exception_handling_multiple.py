total_latency = 1000
latency_ms = 400
number_of_requests = 4

try:
    average = total_latency / number_of_requests
    average_ms = latency_ms / number_of_requests
    print("Average latency is: " + str(average))
    print("Average latency in ms is: " + str(average_ms))
except ZeroDivisionError:
    print("Unable to calculate average latency due to zero requests.")
except TypeError as error:
    print("Unable to calculate average latency due to type error.")
    print("Error: " + str(error))
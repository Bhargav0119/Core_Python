total_latency = 1000
number_of_requests = 0

try:
    average = total_latency / number_of_requests
    print("Average latency is: " + str(average))
except ZeroDivisionError as error:
    print("Unable to calculate average latency due to zero requests.")
    print ("Error: " + str(error))
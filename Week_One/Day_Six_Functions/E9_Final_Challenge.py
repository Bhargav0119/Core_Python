def evaluate_agent_latency(total_latency, number_of_requests):

    try:
        average_latency = total_latency / number_of_requests

        if average_latency > 500:
            return "High latency"
        elif average_latency > 300:
            return "Moderate latency"
        else:
            return "Normal latency"

    except ZeroDivisionError:
        return "No requests available"
    except TypeError:
        return "Invalid input type"

# result = evaluate_agent_latency(3000,4)
# result = evaluate_agent_latency(1600,4)
# result = evaluate_agent_latency(1000,4)

print(evaluate_agent_latency(3000, 4))
print(evaluate_agent_latency(1600, 4))
print(evaluate_agent_latency(1000, 4))
print(evaluate_agent_latency("3000", 4))

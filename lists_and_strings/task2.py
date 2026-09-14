import math
measures = [10, 10.1, 9.9, 9.6, 10.1, 9.9, 9.8, 9.9, 10.3, 10]

total = 0
for value in measures:
    total = total + value

average = total / len(measures)
print("Average: ", average)

sum_squared_differences = 0
for value in measures:
    difference = value - average
    sum_squared_differences = sum_squared_differences + (difference * difference)
    
variance = sum_squared_differences / len(measures)
std_dev = math.sqrt(variance)

print(f"Standard Deviation: {std_dev:.2f}")


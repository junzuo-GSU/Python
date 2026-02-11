"""
Chapter 3 - Assignment program 1
Date: 1/28/2026
This Python program simulates monitoring network bandwidth usage and identifies potential issues, 
using control statements and formatted output.
"""

import random

#Constants
NORMAL = "Normal"
HIGH_USAGE = "HIGH USAGE!"
High_USAGE_THRESHOLD = 80.0

# Input: Get monitoring duration
hours = int(input("Monitoring duration (hours): "))

print("=== NETWORK BANDWIDTH MONITOR ===\n")
print("Starting monitoring for " + str(hours) + " hours \n")

# Initialize tracking variables
total_bandwidth = 0
high_usage_hours = 0
highest_bandwidth = 0

# Display table header
print("{:^4}  {:^18}  {:^12}".format("Hour","Bandwidth Usage %","Status"))
print("-" * 40)

# Monitor for specified hours
for hour in range(1, hours + 1):
    bandwidth = round(random.uniform(0, 100), 1)
    total_bandwidth += bandwidth
    
    if bandwidth > highest_bandwidth:
        highest_bandwidth = bandwidth
    
    status = NORMAL
    if bandwidth > High_USAGE_THRESHOLD:
        status = HIGH_USAGE
        high_usage_hours += 1
    
    print("{:^4}  {:^15}  {:^12}".format(hour,bandwidth,status))

# Calculate average
average_bandwidth = total_bandwidth / hours

# Display summary
print("\n" + "="*40)
print("MONITORING SUMMARY")
print("="*40)

print("Monitoring period: " + str(hours) + " hours")
print("Highest bandwidth: " + "{:.1f}".format(highest_bandwidth) + "%")
print("Hours above " + str(High_USAGE_THRESHOLD) + "%: " + str(high_usage_hours) + " hours")
print("Average bandwidth: " + "{:.1f}".format(average_bandwidth) + "%")


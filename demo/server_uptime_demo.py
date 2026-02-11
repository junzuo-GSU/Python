'''
Docstring for demo.server_uptime_demo
Author: OpenAI's ChatGPT
Date: 1/28/2026
This program simulates monitoring server uptime over a specified number of months for multiple servers, collecting uptime
'''

import random

server_number = int(input("Enter number of servers to monitor: "))
months = int(input("Enter number of months to monitor: "))

# Initialize tracking variables
server_names = []
uptime_data = []  # This will be a list of lists
averages = []

# Collect data for each server
for server in range(server_number):
    name = input("Enter server name: ")
    server_names.append(name)
    
    monthly_uptime = []
    total_uptime = 0
    
    # generate uptime for each month using random numbers between 90 and 100
    for month in range(months):
        uptime = random.uniform(90.0, 100.0)  # Simulate uptime percentage
        monthly_uptime.append(uptime)
        total_uptime += uptime
    
    # Calculate average for this server
    avg_uptime = total_uptime / months
    averages.append(avg_uptime)
    uptime_data.append(monthly_uptime)

    # Print monthly uptime for this server
    print(f"\nUptime for {name}:")
    for month in range(months):
        print(f"  Month {month + 1}: {monthly_uptime[month]:.2f}%")
    print(f"  Average Uptime: {avg_uptime:.2f}%\n")


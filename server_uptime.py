'''
Name: server_uptime
Assignment 3 
Date: 1/28/2026
Purpose: create a report for summarizing server uptime for a specified period 
'''

#print("=== SERVER UPTIME MONITOR ===\n")

# Input: Get number of servers and number of month for monitoring
num_servers = int(input("Enter number of servers: "))
num_months = int(input("Enter number of months: "))

# Initialize lists to store data
server_names = []
uptime_data = []  # This will be a list of lists
averages = []

# Collect data for each server
for server in range(num_servers):
    print(f"\n--- Server {server + 1} ---")
    name = input("Enter server name: ")
    server_names.append(name)
    
    monthly_uptime = []
    total_uptime = 0
    
    # Collect uptime for each month
    for month in range(num_months):
        uptime = float(input(f"  Month {month + 1} uptime %: "))
        monthly_uptime.append(uptime)
        total_uptime += uptime
    
    # Calculate average for this server
    avg_uptime = total_uptime / num_months
    averages.append(avg_uptime)
    uptime_data.append(monthly_uptime)

# Calculate overall average
overall_total = 0
for avg in averages:
    overall_total += avg
overall_average = overall_total / num_servers

# Display the report
print("\n" + "="*50)
print("UPTIME REPORT")
print("="*50)

# Print header
header = f"{'Server':<15} "
for month in range(num_months):
    header += f"Month{month+1:<7}"
header += "Average"
print(header)
print("-" * (15 + 8 * num_months + 10))

# Print data for each server
for i in range(num_servers):
    # Start with server name
    row = f"{server_names[i]:<15} "
    
    # Add monthly uptime
    for month in range(num_months):
        row += f"{uptime_data[i][month]:<8.2f}"
    
    # Add average
    row += f"{averages[i]:<8.2f}"
    print(row)

# Print summary
print("\n" + "-" * 50)
print(f"Overall average uptime: {overall_average:.2f}%")

# # Check if any server has low uptime
# print("\nSTATUS CHECK:")
# for i in range(num_servers):
#     if averages[i] < 95.0:
#         print(f"  WARNING: {server_names[i]} has low uptime ({averages[i]:.2f}%)")
#     else:
#         print(f"  OK: {server_names[i]} has good uptime ({averages[i]:.2f}%)")
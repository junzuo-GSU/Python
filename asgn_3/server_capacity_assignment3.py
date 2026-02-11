"""
Program: server_countdown.py
Author: Jun Zuo
Date: February 1, 2026
Description: This program simulates monitoring server storage usage and predicts when capacity will be reached,
Goal: Use a while loop to find when server capacity is reached.
"""
import random

#constants
CRITICAL_THRESHOLD = 0.9
WARNING_THRESHOLD = 0.75
CRITICAL_STATUS = "CRITICAL (90%+)"
WARNING_STATUS = "WARNING (75%+)"
HEALTHY_STATUS = "Healthy"

# Inputs
current_storage = float(input("Enter current storage used (TB): "))
limit = float(input("Enter server capacity limit (TB): "))
growth_rate = float(input("Enter expected monthly growth (%) : ")) / 100

month = 0

# Header
print("\n{:>6}{:>20}{:>20}".format("Month", "Storage (TB)", "Status"))
print("-" * 50)

# The while loop: Runs UNTIL the limit is hit
while current_storage < limit:
    month += 1
    
    # Add randomness to the growth (-2% to +5% fluctuation)
    volatility = random.uniform(-0.02, 0.05)
    monthly_increase = current_storage * (growth_rate + volatility)
    
    current_storage += monthly_increase
    
    # Determine status message using selection
    if current_storage > (limit * CRITICAL_THRESHOLD):
        status = CRITICAL_STATUS
    elif current_storage > (limit * WARNING_THRESHOLD):
        status = WARNING_STATUS
    else:
        status = HEALTHY_STATUS
        
    print("{:>6d}{:>20.2f}{:>20}".format(month, current_storage, status))

# Final Summary
print("-" * 50)
print(f"CRITICAL: Server will reach capacity in {month} months.")
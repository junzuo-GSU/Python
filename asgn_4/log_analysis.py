'''
Assignment: 2
Name: log_analysis.py
Author: June Zuo
Date: 1/24/26
Purpose: Analyze log messages and calculate storage requirements using math module
''' 
#imports
import math

#constants
CONVERSION_KB = 1024  # 1 KB = 1024 Bytes

# user inputs
log_message = input('Enter the log message: ') #"ERROR: Disk write failure at 3:45 PM"
num_messages = int(input('Enter the number of log messages: '))

# Basic analysis
message_length = len(log_message)
total_bytes = num_messages * message_length
total_kilobytes = total_bytes / CONVERSION_KB

# Use math.ceil() to round UP to nearest whole kilobyte
# This is practical for system administration - we always round up for storage
rounded_kb = math.ceil(total_kilobytes)
rounded_down_kb = math.floor(total_kilobytes)

# Print results
print("=== LOG STORAGE CALCULATOR ===")
print()
print("Log message: " + log_message)
print("Message length: " + str(message_length) + " characters")
print()
print("Storage for " + str(num_messages) + " messages:")
print("Exact kilobytes: " + str(total_kilobytes))
print("Rounded UP (ceil): " + str(rounded_kb) + " KB")
print("Rounded DOWN (floor): " + str(rounded_down_kb) + " KB")
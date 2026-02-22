'''
Docstring for asgn_4.log_manager_copy

This script is going to read a file named "raw_usage.txt" that contains lines of the format "username:usage_in_MB". 
It will then generate a report in "usage_report.txt" that lists each user, their usage, and whether they are over a specified limit (500 MB). 
The report will also include a total usage.
'''
# Constants for easy configuration
LIMIT = 500
STATUS_OVER = "OVER LIMIT"
STATUS_OK = "OK"

# Get filenames from the user
input_filename = input("Enter the name of the input file (e.g., data.txt): ")
output_filename = input("Enter the name for the output file (e.g., results.txt): ")

total_usage = 0

# Using 'with' to manage both files safely
with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    for line in infile:
        # Clean up the line and split into parts
        line = line.strip()
        parts = line.split(":")
        
        # Assign variables from the split list
        username = parts[0]
        usage = int(parts[1])
        
        # Determine status using our constants
        if usage > LIMIT:
            status = STATUS_OVER
        else:
            status = STATUS_OK
        
        # Format the line with f-strings for a tabular look
        # :<10 aligns left with 10 spaces, :>5 aligns right with 5 spaces
        output_line = f"User: {username:<10} | Usage: {usage:>5} | Status: {status}\n"
        
        # Write to file and update the total
        outfile.write(output_line)
        total_usage += usage

# Final summary output to the console
print("-" * 30)
print(f"Processing complete. Details saved to: {output_filename}")
print(f"Total Disk Usage for all users: {total_usage} MB")
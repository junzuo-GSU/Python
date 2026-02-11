"""
Assignment: Server Log & Quota Manager
Description: Reads usage data, checks against a limit, 
and writes a formatted summary report.
"""
import os

input_file = "raw_usage.txt"
output_file = "usage_report.txt"
limit = 500
total_usage = 0

# 1. Check if the file exists before proceeding
if not os.path.exists(input_file):
    print(f"Error: {input_file} not found in {os.getcwd()}")
    exit()

# 2. Read from the input file and process data
with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    # Write the header to the output file
    f_out.write(f"{'--- SYSTEM QUOTA REPORT ---':^40}\n")
    f_out.write(f"{'USER':<15} | {'USAGE':<8} | {'STATUS'}\n")
    f_out.write("-" * 40 + "\n")

    for line in f_in:
        # Strip whitespace and skip empty lines
        line = line.strip()
        if not line:
            continue

        # 3. String Manipulation: Split into Name and Number
        parts = line.split(":")
        username = parts[0]
        usage_mb = int(parts[1]) # Convert numeric text to integer
        
        total_usage += usage_mb

        # 4. Logic check for Status
        if usage_mb > limit:
            status = "OVER LIMIT"
        else:
            status = "OK"

        # 5. Write formatted text to the report file
        f_out.write(f"{username:<15} | {usage_mb:>5} MB | {status}\n")

    # 6. Write the final numeric summary
    f_out.write("-" * 40 + "\n")
    f_out.write(f"TOTAL SERVER USAGE: {total_usage} MB\n")

print(f"Report successfully generated: {output_file}")


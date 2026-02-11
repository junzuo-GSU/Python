'''
Assignment: 2
Name: disk_usage.py
Author: June Zuo
Date: 1/24/26
Purpose: Convert disk usage from KB to MB and GB, and display a formatted report.
'''

# Conversion constants
KB_TO_MB = 1024  # 1 MB = 1024 KB
MB_TO_GB = 1024  # 1 GB = 1024 MB

# User inputs
usage_kb = int(input("Enter disk usage in Kilobytes (KB): "))

# Perform conversions
usage_mb = usage_kb / KB_TO_MB
usage_gb = usage_mb / MB_TO_GB

# Display formatted report
print("Disk Usage Report for User:")
print("=" * 35)
print("Usage in Kilobytes  (KB): " + str(usage_kb))
print("Usage in Megabytes (MB): " + str(round(usage_mb, 2)))
print("Usage in Gigabytes (GB): " + str(round(usage_gb, 2)))

quota_gb = 50  # 50 GB quota
remaining_gb = quota_gb - usage_gb

print("\nQuota Analysis:")
print("-" * 20)
print("Quota: " + str(quota_gb) + " GB")
print("Used: " + str(round(usage_gb, 2)) + " GB")
print("Remaining: " + str(round(remaining_gb, 2)) + " GB")

# Calculate percentage
percentage_used = (usage_gb / quota_gb) * 100
print("Percentage used: " + str(round(percentage_used, 1)) + "%")
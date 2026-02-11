"""
Program: investment.py
Author: Fundamentals of Python: First Programs
Compute an investment report.
"""

# Input: Receive the user's inputs and initialize data
start_balance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))

# Convert rate to a decimal
rate = rate / 100

# Initialize totals
total_interest = 0.0

# Display the table's header, Using field widths: 4, 18, 10, 16
#header = "%4s%18s%10s%16s" % ("Year", "Starting Balance", "Interest", "Ending Balance")
header = "{:>4}{:>18}{:>10}{:>16}".format(
    "Year", "Starting Balance", "Interest", "Ending Balance"
)
print(header)

# Compute the results for each year and display them
for year in range(1, years + 1):
    interest = start_balance * rate
    end_balance = start_balance + interest
    
    # Format the row data
    #print("%4d%18.2f%10.2f%16.2f" % (year, start_balance, interest, end_balance))
    print("{:>4d}{:>18.2f}{:>10.2f}{:>16.2f}".format(
        year, start_balance, interest, end_balance
    ))
    
    # Update totals and balance for the next year
    total_interest += interest
    start_balance = end_balance

# Display the summary totals
print("\nEnding balance: $%0.2f" % start_balance)
print("Total interest earned: $%0.2f" % total_interest)
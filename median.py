"""
File: median.py
Prints the median of a set of numbers in a file.
"""

fileName = input("Enter the filename: ")

# Using 'with' ensures the file is closed automatically
numbers = []
with open(fileName, 'r') as f:
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))

# Sort the list to find the median
numbers.sort()

if len(numbers) == 0:
    print("The file is empty.")
else:
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        # Odd number of elements
        median = numbers[midpoint]
    else:
        # Even number of elements: average of the two middle values
        median = (numbers[midpoint] + numbers[midpoint - 1]) / 2
        
    print("The median is", median)
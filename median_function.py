"""
median.py
Provides three functions and a main() to compute the median of numbers in a file.

Functions:
- get_numbers_from_file(filename) -> list[float]
- find_median(numbers) -> float | None
- print_results(median) -> None

Main-line logic is inside `main()`.
"""

def get_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            for number in line.split():
                    numbers.append(float(number))
    return numbers


def find_median(numbers):
    nums = sorted(numbers)
    n = len(nums)
    mid = n // 2
    if n % 2 == 1:
        return nums[mid]
    else:
        return (nums[mid - 1] + nums[mid]) / 2.0


def print_results(median):
    if median is None:
        print("The file contains no numeric data.")
    else:
        print(f"The median is {median}")


def main():
    filename = input("Enter the filename: ")
    
    numbers = get_numbers_from_file(filename)
    median = find_median(numbers)
    print_results(median)


if __name__ == '__main__':
    main()
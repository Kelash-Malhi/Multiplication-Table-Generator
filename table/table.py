# Task Title: Multiplication Table Generator

# Description:
# The program takes at least 2 numbers from the user and prints
# their multiplication tables from 1 to 10.
# If less than 2 numbers are entered, show a warning message.

# Get input from user (comma-separated)
numbers_input = input("Enter at least 2 numbers separated by commas: ")

# Convert to list of integers
numbers = [int(num.strip()) for num in numbers_input.split(",") if num.strip().isdigit()]

# Check if at least 2 numbers are entered
if len(numbers) < 2:
    print("Still not accepted! You must enter at least 2 or more values.")
else:
    # Print multiplication table for each number
    for num in numbers:
        print(f"\nTable of {num}")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

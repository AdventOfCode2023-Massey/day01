# Advent of Code 2023 Day 1 Part 1
# Code by Github Copilot Chat
# Editing by Bart Massey

def sum_calibration_values_from_file(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            first_digit = next((char for char in line if char.isdigit()), None)
            last_digit = next((char for char in reversed(line) if char.isdigit()), None)
            if first_digit and last_digit:
                total += int(first_digit + last_digit)
    return total

print(sum_calibration_values_from_file('input.txt'))

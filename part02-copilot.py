# Advent of Code 2023 Day 1 Part 2
# Code by Github Copilot Chat
# Editing by Bart Massey

# This initial solution assumes that the words and numbers
# could be obtained by splitting on whitespace.

def sum_calibration_values_from_file(file_path):
    digit_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            first_digit = last_digit = None
            for word in line.split():
                if word.isdigit():
                    if first_digit is None:
                        first_digit = word
                    last_digit = word
                elif word in digit_map:
                    if first_digit is None:
                        first_digit = digit_map[word]
                    last_digit = digit_map[word]
            if first_digit and last_digit:
                total += int(first_digit + last_digit)
    return total

print(sum_calibration_values_from_file('input.txt'))

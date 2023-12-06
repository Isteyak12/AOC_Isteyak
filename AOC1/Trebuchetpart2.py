import re

# Dictionary mapping spelled-out digits to their numeric equivalents
replacements = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def extract_calibration_value(line):
    digits = re.findall(r'\d+|one|two|three|four|five|six|seven|eight|nine', line)
    real_digits = [replacements.get(digit, digit) for digit in digits if digit.isdigit() or digit in replacements]

    if len(real_digits) >= 2:
        return int(real_digits[0] + real_digits[-1])
    elif len(real_digits) == 1:
        return int(real_digits[0]) * 2
    else:
        return 0

result = 0

with open('1input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        calibration_value = extract_calibration_value(line)
        result += calibration_value

print("The sum of all calibration values:", result)

def extract_calibration_value(line):
    digits = ''.join(filter(str.isdigit, line))  # Extract digits from the line
    if len(digits) >= 2:
        return int(digits[0] + digits[-1])  # Combine first and last digits
    elif len(digits) == 1:
        return int(digits * 2)  # Duplicate the single digit
    else:
        return 0  # Return 0 if there are no digits in the line

result = 0

with open('1input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        calibration_value = extract_calibration_value(line)
        result += calibration_value

print("The sum of all calibration values:", result)

def find_adjacent_number(string, symbol):
    numbers = [int(s) for s in string.split() if s.isdigit()]
    symbol_index = string.find(symbol)
    adjacent_numbers = []

    for number in numbers:
        number_index = string.find(str(number))
        if abs(number_index - symbol_index) == 1:
            adjacent_numbers.append(number)

    return adjacent_numbers

# Example usage
test_string = "A quick 5 brown 76 foxes jump 7 over 8 the lazy dog."
target_symbol = "6"

result = find_adjacent_number(test_string, target_symbol)
print(f"The numbers adjacent to '{target_symbol}' are: {result}")

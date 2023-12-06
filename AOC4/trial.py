def calculate_points():
    total = 0
    try:
        with open('input.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split('|')
                if len(parts) == 2:
                    x, y = map(str.split, parts)
                    matches = set(x) & set(y)
                    total += 2 ** (len(matches) - 1) if matches else 0
                else:
                    print(f"Issue with line format: {line.strip()}")
    except FileNotFoundError:
        print("File not found!")
    return total

print(calculate_points())

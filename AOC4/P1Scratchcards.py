def calculate_points(card):
    winning_numbers = set(card[:5])
    your_numbers = set(card[5:])
    
    matches = your_numbers.intersection(winning_numbers)
    
    points = 0
    match_count = len(matches)
    if match_count > 0:
        points = 2 ** (match_count - 1)
    
    return points

def total_points_all_cards(cards):
    total_points = sum(calculate_points(card) for card in cards)
    return total_points

# Define the scratchcards data as an array of arrays
scratchcards_data = [
    [41, 48, 83, 86, 17, 83, 86, 6, 31, 17, 9, 48, 53],
    [13, 32, 20, 16, 61, 61, 30, 68, 82, 17, 32, 24, 19],
    [1, 21, 53, 59, 44, 69, 82, 63, 72, 16, 21, 14, 1],
    [41, 92, 73, 84, 69, 59, 84, 76, 51, 58, 5, 54, 83],
    [87, 83, 26, 28, 32, 88, 30, 70, 12, 93, 22, 82, 36],
    [31, 18, 13, 56, 72, 74, 77, 10, 23, 35, 67, 36, 11]
]
print(scratchcards_data)

for idx, card in enumerate(scratchcards_data, start=1):
    print(f"Card {idx}: {card}")

total_points = total_points_all_cards(scratchcards_data)
print(f"The total points for the scratchcards are: {total_points}")

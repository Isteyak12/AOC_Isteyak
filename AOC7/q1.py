# Function to convert card label to a numeric value for comparison
def card_value(card):
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    return card_values.get(card, 11 if card.isalpha() else int(card))

# Function to compare two hands based on their strength
def compare_hands(hand1, hand2):
    for i in range(5):
        if card_value(hand1[i]) != card_value(hand2[i]):
            return card_value(hand1[i]) - card_value(hand2[i])
    return 0

# Dictionary to map hand types to their ranks
hand_ranks = {
    'Five of a kind': 1,
    'Four of a kind': 2,
    'Full house': 3,
    'Three of a kind': 4,
    'Two pair': 5,
    'One pair': 6,
    'High card': 7
}

# Function to determine the type of hand
def hand_type(hand):
    card_counts = {card: hand.count(card) for card in hand}
    max_count = max(card_counts.values())

    if max_count == 5:
        return 'Five of a kind'
    elif max_count == 4:
        return 'Four of a kind'
    elif max_count == 3:
        if len(card_counts) == 2:
            return 'Full house'
        return 'Three of a kind'
    elif max_count == 2:
        if len(card_counts) == 3:
            return 'Two pair'
        return 'One pair'
    return 'High card'

# Read data from file
file_name = 'input.txt'  # Replace with your file name

hands = []
bids = []

with open(file_name, 'r') as file:
    for line_num, line in enumerate(file, start=1):
        data = line.strip().split()
        if len(data) >= 2:
            hands.append(data[0])
            bids.append(int(data[1]))
        else:
            print(f"Invalid data format in line {line_num}: {line.strip()}")

if len(hands) != len(bids):
    print("Error: Number of hands and bids do not match.")
else:
    # Pair hands with their bids and sort them by hand strength
    hand_bids = list(zip(hands, bids))
    hand_bids.sort(key=lambda x: (hand_ranks[hand_type(x[0])], card_value(max(x[0]))), reverse=True)

    # Calculate winnings for each hand based on rank and bid
    total_winnings = sum(bid * (i + 1) for i, (_, bid) in enumerate(hand_bids))

    print("Total Winnings:", total_winnings)

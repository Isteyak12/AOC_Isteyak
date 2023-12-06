# Assuming the file is named game_records.txt
file_path = 'input.txt'

def read_game_records(file_path):
    game_records = []
    with open(file_path, 'r') as file:
        for line in file:
            game_records.append(line.strip())  # Remove leading/trailing whitespaces
            
    return game_records

# Read the game records from the file
game_records = read_game_records(file_path)

# Now you can use the game_records list in the previous code to process the games
# (You can use the code provided in the previous example here)

def check_possible_games(game_records, red_cubes, green_cubes, blue_cubes):
    possible_games = []
    
    for record in game_records:
        game_id, cubes_info = record.split(': ')
        cubes = cubes_info.split('; ')
        
        red_total = 0
        green_total = 0
        blue_total = 0
        
        for subset in cubes:
            subset_cubes = subset.split(', ')
            for cube in subset_cubes:
                num, color = cube.split()
                num = int(num)
                
                if color == 'red':
                    red_total += num
                elif color == 'green':
                    green_total += num
                elif color == 'blue':
                    blue_total += num
        
        if red_total <= red_cubes and green_total <= green_cubes and blue_total <= blue_cubes:
            possible_games.append(int(game_id.split()[1]))
    
    return possible_games

# Read game records from a text file
file_path = 'input.txt'  # Replace with your file path
with open(file_path, 'r') as file:
    game_records = file.readlines()

red_cubes = 12
green_cubes = 13
blue_cubes = 14

# Remove newline characters and whitespace
game_records = [record.strip() for record in game_records]

possible_games = check_possible_games(game_records, red_cubes, green_cubes, blue_cubes)
sum_possible_games = sum(possible_games)

print("Possible games:", possible_games)
print("Sum of IDs for possible games:", sum_possible_games)

def follow_instructions(pattern, network):
    current_node = 'AAA'  # Starting node
    steps = 0

    for direction in pattern:
        left_node, right_node = network[current_node]
        current_node = right_node if direction == 'R' else left_node
        steps += 1

        if current_node == 'ZZZ':
            return steps  # Return the number of steps once ZZZ is reached

    return -1  # If ZZZ isn't reached after iterating through the pattern, return -1

def main():
    file_name = 'input.txt'  # Replace with your input file name

    with open(file_name, 'r') as file:
        pattern = file.readline().strip()  # Read the pattern from the first line

        # Define the network structure as a dictionary of nodes and connections
        network = {}
        for line in file:
            parts = line.strip().split(' = ')
            if len(parts) != 2:
                print(f"Issue with line: {line.strip()}")  # Print problematic lines
                continue

            node = parts[0]
            connections = parts[1][1:-1].split(', ')
            network[node] = tuple(connections)

    steps = follow_instructions(pattern, network)
    if steps != -1:
        print(f"Steps required to reach ZZZ: {steps}")
    else:
        print("ZZZ not reached with the given pattern.")

if __name__ == "__main__":
    main()

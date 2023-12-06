import regex as re
from dataclasses import dataclass

@dataclass
class PartNumber:
	value: int
	row: int
	start: int
	end: int

@dataclass
class Bounds:
	up: int
	down: int
	left: int
	right: int


with open("input.txt", 'r') as file:
	strings = file.read().splitlines()

part_numbers = []

output = 0
for row, string in enumerate(strings):
	nums = [int(x) for x in re.findall(r'\d+', string)]

	start = 0
	for pos, c in enumerate(string):
		if c.isdigit():
			if start == 0:
				start = pos
			if pos == len(string) - 1:
				part_numbers.append(PartNumber(
					nums.pop(0), row, start, pos
				))
				start = 0
				continue
			elif not string[pos + 1].isdigit():
				part_numbers.append(PartNumber(
					nums.pop(0), row, start, pos
				))
				start = 0
				continue
	
for part_number in part_numbers:
	surrounding = ''

	num = part_number.value
	row = part_number.row
	start = part_number.start
	end = part_number.end

	bounds = Bounds(
		row != 0,
		row != len(strings) - 1,
		start != 0,
		end != len(strings) - 1
	)

	if bounds.up: surrounding += strings[row - 1][start - bounds.left:end + bounds.right + 1] + '\n'
	surrounding += strings[row][start - bounds.left:end + bounds.right + 1] + '\n'
	if bounds.down: surrounding += strings[row + 1][start - bounds.left:end + bounds.right + 1]

	surrounding = surrounding.replace(".", '').strip()
	surrounding = "".join([x for x in surrounding if not x.isdigit()])

	if len(surrounding) > 0:
		output += num

print(output)
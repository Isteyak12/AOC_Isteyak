import regex as re

lookup_table = {
    'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0', '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'
}

inpFile = 'note.txt'
with open(inpFile, 'r') as f:
    text = f.read().splitlines()

digit_lists = [re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine|zero)', i, overlapped=True) for i in text]
digit_lists = [[lookup_table[j] for j in i] for i in digit_lists]

nums = [int(i[0]+i[-1]) for i in digit_lists]

print(sum(nums))
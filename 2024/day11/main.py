TESTFILE_NAME = "test.txt"
INPUTFILE_NAME = "input.txt"

with open(INPUTFILE_NAME) as f:
    input_data = f.readline()
    stones = input_data.strip().split()

blinks = 1000
stones = list(map(int, stones))
stone_map = {}


def add_to_dict(dictionary, stone, value):
    if stone in dictionary:
        dictionary[stone] += value
    else:
        dictionary[stone] = value
    return dictionary


for stone in stones:
    add_to_dict(stone_map, stone, 1)
        
for _ in range(blinks):
    new_stone_map = {}
    for stone, amount in stone_map.items():
        if stone == 0:
            add_to_dict(new_stone_map, 1, amount)
        elif len(str(stone)) % 2 == 0:
            digits = str(stone)
            half_digits = len(digits) // 2
            add_to_dict(new_stone_map, (int(digits[:half_digits])), amount)
            add_to_dict(new_stone_map, (int(digits[half_digits:])), amount)
        else:
            add_to_dict(new_stone_map, stone*2024, amount)
    stone_map = new_stone_map.copy()

print(sum(stone_map.values()))

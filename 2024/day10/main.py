TESTFILE_NAME = "test_part_2.txt"
INPUTFILE_NAME = "input.txt"


def find_tops(hiking_map, x, y, x_max, y_max, target, top):  # noqa: PLR0913
    tops = []
    for direction in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
        if is_out_of_bounds(direction, x_max, y_max):
            continue

        if hiking_map[direction[1]][direction[0]] == top and target == hiking_map[direction[1]][direction[0]]:
            tops.append(direction)
        
        if hiking_map[direction[1]][direction[0]] == target:
            tops.extend(find_tops(hiking_map, direction[0], direction[1], x_max, y_max, target + 1, top))

    return tops
        
    
def is_out_of_bounds(direction, x_max, y_max):
    x, y = direction
    return x < 0 or y < 0 or x >= x_max or y >= y_max


with open(INPUTFILE_NAME) as f:
    input_data = f.readlines()

# Part one
hiking_map = []
x_max = 0
y_max = len(input_data)
for levels in input_data:
    x_max = len(levels)
    hiking_stroke = []
    for level in levels.strip():
        hiking_stroke.append(int(level))
    hiking_map.append(hiking_stroke)

tops_1 = 0
tops_2 = 0
for y, levels in enumerate(hiking_map):
    for x, level in enumerate(levels):
        # Found trail-head
        if level == 0:
            tops = find_tops(hiking_map, x, y, x_max, y_max, target=1, top=9)
            tops_2 += len(tops)
            tops_1 += len(list(dict.fromkeys(find_tops(hiking_map, x, y, x_max, y_max, target=1, top=9))))
        
print(tops_1)
print(tops_2)

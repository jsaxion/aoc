TESTFILE_NAME = "test.txt"
INPUTFILE_NAME = "input.txt"


def is_out_of_bounds(x, y, x_max, y_max):
    return x < 0 or y < 0 or x >= x_max or y >= y_max


def calc_anti_nodes_part_1(position, positions, x_max, y_max):
    anti_nodes = set()
    for opposite_position in positions:
        # Can be optimized to do this already
        if position is opposite_position:
            continue
        x, y = position
        xx, yy = opposite_position
        an_x, an_y = (xx - (x - xx), yy - (y - yy))
        if not is_out_of_bounds(an_x, an_y, x_max, y_max):
            anti_nodes.add((an_x, an_y))
    return anti_nodes


def calc_anti_nodes_part_2(position, positions, x_max, y_max):
    anti_nodes = set()
    for opposite_position in positions:
        # Can be optimized to do this already
        if position is opposite_position:
            continue
        x, y = position
        xx, yy = opposite_position
        an_x, an_y = (xx, yy)
        while not is_out_of_bounds(an_x, an_y, x_max, y_max):
            anti_nodes.add((an_x, an_y))
            an_x, an_y = an_x - (x - xx), an_y - (y - yy)
    return anti_nodes


with open(TESTFILE_NAME) as f:
    input_data = f.readlines()

# Part one
anti_nodes = set()
antennas = []
antenna_layout = {}
y_max = len(input_data)
for y, antennas in enumerate(input_data):
    for x, antenna in enumerate(antennas.strip()):
        if antenna in {'.', '#'}:
            continue
        if antenna_layout.get(antenna) is not None:
            antenna_layout[antenna].append((y, x))
        else:
            antenna_layout[antenna] = [(y, x)]

x_max = len(antennas)
for positions in antenna_layout.values():
    for position in positions:
        # anti_nodes.update(calc_anti_nodes_part_1(position, positions, x_max, y_max))
        anti_nodes.update(calc_anti_nodes_part_2(position, positions, x_max, y_max))

print(anti_nodes)
print(len(anti_nodes))

# Function to print results
for x in range(x_max):
    for y in range(y_max):
        for character, values in antenna_layout.items():
            if (x, y) in values:
                print(character, end="")
                break
        else:
            if (x, y) in anti_nodes:
                print("#", end="")
            else:
                print(".", end="")
    print()

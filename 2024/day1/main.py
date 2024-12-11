TESTFILE_NAME = "test.txt"
INPUTFILE_NAME = "input.txt"

left = []
right = []

with open(INPUTFILE_NAME) as f:
    for line in f.readlines():
        left_part, right_part = line.strip().split("   ")
        left.append(int(left_part))
        right.append(int(right_part))
left.sort()
right.sort()

# Part one
total = 0
for i, left_value in enumerate(left):
    total += abs(left_value - right[i])
print(f"Part a: {total}")

# Part two
similarity_score = 0
for value in left:
    similarity_score += value * right.count(value)

print(f"Part b: {similarity_score}")

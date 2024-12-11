import re


TESTFILE_NAME = "test.txt"
INPUTFILE_NAME = "input.txt"


with open(INPUTFILE_NAME) as f:
    input_data = f.readlines()

# Part one
result = 0
multiplications = []
for line in input_data:
    multiplications.extend(re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", line))
for multiplication in multiplications:
    x, y = multiplication[4:-1].split(",")
    result += int(x) * int(y)

print(f"Result: {result}")

# Part two
result = 0
findings = []
one_big_line = ""
for line in input_data:
    one_big_line += line

enabled = True
findings.extend(re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|don\'t\(\)|do\(\)", one_big_line))
for finding in findings:
    if finding.startswith("do("):
        enabled = True
    elif finding.startswith("don"):
        enabled = False
    elif enabled:
        x, y = finding[4:-1].split(",")
        result += int(x) * int(y)

print(f"Result: {result}")

import operator

TESTFILE_NAME = "test.txt"
INPUTFILE_NAME = "input.txt"

OPERATORS = [operator.add, operator.mul, operator.concat]


def calc_results(expected_result, values, result):
    if len(values) == 0 and expected_result == result:
        return True
    if len(values) == 0:
        return False
    value = values.pop(0)
    for op in OPERATORS:
        if op == operator.concat:
            tmp_result = int(op(str(result), str(value))) # type: ignore
        else:
            tmp_result = op(result, value)
        if calc_results(expected_result, values.copy(), tmp_result):
            return True
    return False


with open(INPUTFILE_NAME) as f:
    input_data = f.readlines()

# Part one
total_result = 0
calibrations = []
for line in input_data:
    result, values = line.split(":")
    values = list(map(int, values.strip().split(" ")))
    calibrations.append((int(result), values))

for calibration in calibrations:
    expected_result, values = calibration
    first_value = values.pop(0)
    if calc_results(expected_result, values, first_value):
        total_result += expected_result


print(f"Result: {total_result}")

# Part two
print(f"Result: {total_result}")

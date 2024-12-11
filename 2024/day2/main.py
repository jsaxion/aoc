TESTFILE_NAME = "test.txt"
INPUTFILE_NAME = "input.txt"


reports = []

with open(INPUTFILE_NAME) as f:
    for line in f:
        reports.append(list(map(int, line.strip().split(" "))))

# Part one
safe_reports = 0
for report in reports:
    for i, level in enumerate(report):
        if ((all(level <= report[i+1] for i in range(len(report) - 1)) or
            all(level >= report[i+1] for i in range(len(report) - 1))) and
            all((abs(level - report[i+1]) >= 1 and abs(level - report[i+1]) <= 3) for i in range(len(report) - 1))
        ):
            safe_reports += 1

# Part two
safer_reports = 0
for report in reports:
    for i, level in enumerate(report):
        del report[i]  # noqa: B909
        if ((all(report[i] <= report[i+1] for i in range(len(report) - 1)) or
             all(report[i] >= report[i+1] for i in range(len(report) - 1))) and
             all((abs(report[i] - report[i+1]) >= 1 and abs(report[i] - report[i+1]) <= 3) for i in range(len(report) - 1))
        ):
            safer_reports += 1
            break
        report.insert(i, level)  # noqa: B909

print(f"Safe reports: {safe_reports}, safer reports: {safer_reports}")

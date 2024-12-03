from utils import read_input

def p1(input: str):
    count = 0
    for line in input.splitlines():
        report = [int(elem) for elem in line.split(" ")]
        if is_decrease(report) or is_increase(report):
            count += 1

    print(count)

def p2(input: str):
    count = 0
    for line in input.splitlines():
        report = [int(elem) for elem in line.split(" ")]
        if check_p2(report, is_increase) or check_p2(report, is_decrease):
            count += 1
    print(count)

def check_p2(report: list[int], func):
    for i in range(len(report)):
        copy = report.copy()
        del copy[i]
        if func(copy):
            return True
    return False

def is_increase(report: list[int]):
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        if diff < 1 or diff > 3:
            return False
    return True

def is_decrease(report: list[int]):
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        if diff < -3 or diff > -1:
            return False
    return True

def main():
    input_2 = "input-2"
    p2(read_input(input_2))
    # p2(read_input(input_1))

if __name__ == "__main__":
    main()
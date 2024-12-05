import re
from utils import read_input

def p1(input: str):
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", input)

    sum = 0
    for match in matches:
        chunks = match.split(",")
        first = int(chunks[0][4:])
        second = int(chunks[1][:-1])
        sum += first * second
    print(sum)

def p2(input: str):
    matches = re.findall("(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", input)
    print(matches)
    is_allowed = True
    sum = 0
    for match in matches:
        if match == "do()":
            is_allowed = True
        elif match == "don't()":
            is_allowed = False
        else:
            if is_allowed:
                sum += get_mul_from_match_str(match)
    print(sum)
            
def get_mul_from_match_str(match: str):
    chunks = match.split(",")
    return int(chunks[0][4:]) * int(chunks[1][:-1])

def main():
    input = "input-3"
    p2(read_input(input))

if __name__ == "__main__":
    main()
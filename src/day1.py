from utils import read_input
from collections import Counter

def p1(input: str):
    group_1, group_2 = split_input(input)
    
    group_1.sort()
    group_2.sort()

    sum = 0
    for a, b in zip(group_1, group_2):
        sum += abs(b - a)
    print(sum)

def p2(input: str):
    similarity = 0
    group_1, group_2 = split_input(input)

    group_2_counter = Counter(group_2)
    
    for elem in group_1:
        similarity += elem * group_2_counter[elem]
    print(similarity)

def split_input(input):
    group_1 = []
    group_2 = []
    for line in input.splitlines():
        chunks = line.split()
        group_1.append(int(chunks[0]))
        group_2.append(int(chunks[1]))
    return group_1, group_2

def main():
    input_1 = "input-1"
    # input_1 = "sample"
    # p1(read_input(input_1))
    p2(read_input(input_1))

if __name__ == "__main__":
    main()
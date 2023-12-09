import os
import re
import math

from time import time
from utils.get_input import import_input

example = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

example2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

example3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def part1(text):
    lines = text.splitlines()
    next_element = dict()
    current_element = "AAA"
    instructions = lines[0]
    steps = 0

    for line in lines[2:]:
        source, left, right = re.findall(r"[a-zA-Z]+", line)
        next_element[source] = (left, right)

    while current_element != "ZZZ":
        for i in range(len(instructions)):
            steps += 1
            current_element = next_element[current_element][instructions[i] == "R"]
            if current_element == "ZZZ":
                return steps


def part2(text):
    lines = text.splitlines()
    next_element = dict()
    instructions = lines[0]
    steps = 0
    steps_by_element = []

    for line in lines[2:]:
        source, left, right = re.findall(r"[a-zA-Z0-9]+", line)
        next_element[source] = (left, right)

    current_elements = [el for el in next_element if el.endswith("A")]

    while sum(1 for el in current_elements if el.endswith("Z")) != len(
        current_elements
    ):
        current_new = []

        if steps % 10000 == 0:
            print(steps)

        for i in range(len(instructions)):
            steps += 1
            for e in current_elements:
                current_new.append(next_element[e][instructions[i] == "R"])

                if current_new[-1].endswith("Z"):
                    steps_by_element.append(steps)
                    current_new.pop()

            current_elements = current_new.copy()
            current_new = []

    return math.lcm(*steps_by_element)


if __name__ == "__main__":
    day_num = "".join([n for n in os.path.basename(__file__) if n.isdigit()])
    import_input(day_num)
    input_path = "data/day" + day_num + ".txt"
    text_input = open(input_path, "r").read()

    start_time = time()
    print(f"1. Example :  {part1(example):<20} ({time()-start_time:.3f} s)")
    start_time = time()
    print(f"1. Example2:  {part1(example2):<20} ({time()-start_time:.3f} s)")
    start_time = time()
    print(f"1. Input   :  {part1(text_input):<20} ({time()-start_time:.3f} s)")

    print("-" * 100)

    start_time = time()
    print(f"2. Example3 :  {part2(example3):<20} ({time()-start_time:.3f} s)")
    start_time = time()
    print(f"2. Input   :  {part2(text_input):<20} ({time()-start_time:.3f} s)")

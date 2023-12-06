import os
import re
from functools import reduce
from utils.get_input import import_input

example = """Time:      7  15   30
Distance:  9  40  200"""


def part1(text):
    lines = text.splitlines()

    times = list(map(int, re.findall(r"\d+", lines[0])))
    distances = list(map(int, re.findall(r"\d+", lines[1])))
    win_ways = [0 for _ in range(len(times))]

    for i, t in enumerate(times):
        d = distances[i]
        for speed in range(1, t - 1):
            if d < speed * (t - speed):
                win_ways[i] += 1

    return reduce(lambda a, b: a * b, win_ways)


def part2(text):
    lines = text.splitlines()

    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))

    win_ways_inf = None
    win_ways_sup = None

    for speed in range(1, time - 1):
        if distance < speed * (time - speed):
            win_ways_inf = speed
            break

    for speed in range(time - 1, 1, -1):
        if distance < speed * (time - speed):
            win_ways_sup = speed
            break

    return win_ways_sup - win_ways_inf + 1


if __name__ == "__main__":
    day_num = "".join([n for n in os.path.basename(__file__) if n.isdigit()])
    import_input(day_num)
    input_path = "data/day" + day_num + ".txt"
    text_input = open(input_path, "r").read()

    print("1. Example : ", part1(example))
    print("1. Input : ", part1(text_input))

    print("-" * 100)

    print("2. Example : ", part2(example))
    print("2. Input : ", part2(text_input))

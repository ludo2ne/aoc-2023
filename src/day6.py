import os
import re
from time import time
from functools import reduce
from utils.get_input import import_input

example = """Time:      7  15   30
Distance:  9  40  200"""


def part1(text):
    start_time = time()
    lines = text.splitlines()

    times = list(map(int, re.findall(r"\d+", lines[0])))
    distances = list(map(int, re.findall(r"\d+", lines[1])))
    win_ways = [0 for _ in range(len(times))]

    for i, t in enumerate(times):
        d = distances[i]
        for speed in range(1, t - 1):
            win_ways[i] += d < speed * (t - speed)

    return reduce(lambda a, b: a * b, win_ways), time() - start_time


def part2(text):
    start_time = time()
    lines = text.splitlines()

    times = int(lines[0].split(":")[1].replace(" ", ""))
    distances = int(lines[1].split(":")[1].replace(" ", ""))

    for speed_inf in range(1, times - 1):
        if distances < speed_inf * (times - speed_inf):
            break

    for speed_sup in range(times - 1, 1, -1):
        if distances < speed_sup * (times - speed_sup):
            break

    return speed_sup - speed_inf + 1, time() - start_time


if __name__ == "__main__":
    day_num = "".join([n for n in os.path.basename(__file__) if n.isdigit()])
    import_input(day_num)
    input_path = "data/day" + day_num + ".txt"
    text_input = open(input_path, "r").read()

    print(f"1. Example : {part1(example)[0]:<20} ({part1(example)[1]:.3f} s)")
    print(f"1. Input   : {part1(text_input)[0]:<20} ({part1(text_input)[1]:.3f} s)")

    print("-" * 100)

    print(f"2. Example : {part2(example)[0]:<20} ({part2(example)[1]:.3f} s)")
    print(f"2. Input   : {part2(text_input)[0]:<20} ({part2(text_input)[1]:.3f} s)")

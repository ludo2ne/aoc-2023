import os

from time import time, sleep
from utils.get_input import import_input

example = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def part1(text):
    lines = text.splitlines()
    next_values = []

    for line in lines:
        triangle = [[]]
        triangle[0].extend(map(int, line.split()))

        while not all(v == 0 for v in triangle[-1]):
            r = triangle[-1]
            triangle.append([r[i + 1] - r[i] for i in range(0, len(r) - 1)])

        triangle[-1].append(0)

        for i in range(len(triangle) - 2, -1, -1):
            triangle[i].append(triangle[i][-1] + triangle[i + 1][-1])

        # for t in triangle:
        #    print(*t)

        next_values.append(triangle[0][-1])

    return sum(next_values)


def part2(text):
    lines = text.splitlines()
    next_values = []

    for line in lines:
        triangle = [[]]
        triangle[0].extend(map(int, line.split()))

        while not all(v == 0 for v in triangle[-1]):
            r = triangle[-1]
            triangle.append([r[i + 1] - r[i] for i in range(0, len(r) - 1)])

        triangle[-1].append(0)

        for i in range(len(triangle) - 2, -1, -1):
            triangle[i].insert(0, triangle[i][0] - triangle[i + 1][0])

        # for t in triangle:
        #    print(*t)
        # print()

        next_values.append(triangle[0][0])

    return sum(next_values)


if __name__ == "__main__":
    day_num = "".join([n for n in os.path.basename(__file__) if n.isdigit()])
    import_input(day_num)
    input_path = "data/day" + day_num + ".txt"
    text_input = open(input_path, "r").read()

    start_time = time()
    print(f"1. Example :  {part1(example):<20} ({time()-start_time:.3f} s)")
    start_time = time()
    print(f"1. Input   :  {part1(text_input):<20} ({time()-start_time:.3f} s)")

    print("-" * 100)

    start_time = time()
    print(f"2. Example :  {part2(example):<20} ({time()-start_time:.3f} s)")
    start_time = time()
    print(f"2. Input   :  {part2(text_input):<20} ({time()-start_time:.3f} s)")

import os

from functools import reduce
from utils.get_input import import_input

example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def part1(text):
    lines = text.splitlines()
    total_points = 0

    for line in lines:
        my_numbers, winning_numbers = line[line.index(":") + 1 :].split("|")
        my_numbers = list(map(int, my_numbers.split()))
        winning_numbers = list(map(int, winning_numbers.split()))

        nb_matchs = len(set(my_numbers) & set(winning_numbers))
        total_points += 2 ** (nb_matchs - 1) if nb_matchs else 0

    return total_points


def part2(text):
    lines = text.splitlines()
    lines_copy = [1 for _ in range(len(lines))]

    for index, line in enumerate(lines):
        my_numbers, winning_numbers = line[line.index(":") + 1 :].split("|")
        my_numbers = list(map(int, my_numbers.split()))
        winning_numbers = list(map(int, winning_numbers.split()))

        nb_matchs = len(set(my_numbers) & set(winning_numbers))

        for i in range(index + 1, index + nb_matchs + 1):
            lines_copy[i] += lines_copy[index]

    return reduce(lambda a, b: a + b, lines_copy)


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

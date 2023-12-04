import os
from utils.get_input import import_input

example = """paste_here"""


def part1(text):
    lines = text.splitlines()
    return None


def part2(text):
    lines = text.splitlines()
    return None


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

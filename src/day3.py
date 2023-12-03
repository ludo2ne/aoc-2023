import os

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def part1(text):
    lines = text.splitlines()
    symbols = set()
    total_numbers = 0

    for index, line in enumerate(lines):
        for c in line:
            if not c.isdigit() and c != ".":
                symbols.add(c)

    for index, line in enumerate(lines):
        i = 0
        while i < len(line):
            adjacent_symbol = False
            if line[i].isdigit():
                j = i + 1
                number = line[i]
                while j < len(line) and line[j].isdigit():
                    number += line[j]
                    j += 1
                if (
                    line[max(i - 1, 0)] in symbols
                    or line[min(j, len(line) - 1)] in symbols
                ):
                    adjacent_symbol = True

                for k in range(max(i - 1, 0), min(j, len(line) - 1) + 1):
                    if (
                        lines[max(index - 1, 0)][k] in symbols
                        or lines[min(index + 1, len(lines) - 1)][k] in symbols
                    ):
                        adjacent_symbol = True
                i = j

                if adjacent_symbol:
                    total_numbers += int(number)

            i += 1

    return total_numbers


def part2(text):
    lines = text.splitlines()
    symbol = "*"
    symbol_pos = dict()
    gear_ratio = 0

    for index, line in enumerate(lines):
        for i, c in enumerate(line):
            if c == symbol:
                symbol_pos[(index, i)] = []

    for index, line in enumerate(lines):
        i = 0
        while i < len(line):
            if line[i].isdigit():
                j = i + 1
                number = line[i]
                while j < len(line) and line[j].isdigit():
                    number += line[j]
                    j += 1
                number = int(number)
                if line[max(i - 1, 0)] == symbol:
                    symbol_pos[index, max(i - 1, 0)].append(number)
                if line[min(j, len(line) - 1)] == symbol:
                    symbol_pos[index, min(j, len(line) - 1)].append(number)

                for k in range(max(i - 1, 0), min(j, len(line) - 1) + 1):
                    if lines[max(index - 1, 0)][k] == symbol:
                        symbol_pos[max(index - 1, 0), k].append(number)

                    if lines[min(index + 1, len(lines) - 1)][k] == symbol:
                        symbol_pos[min(index + 1, len(lines) - 1), k].append(number)
                i = j
            i += 1

    for x in symbol_pos.values():
        if len(x) == 2:
            gear_ratio += x[0] * x[1]

    return gear_ratio


if __name__ == "__main__":
    day_num = "".join([n for n in os.path.basename(__file__) if n.isdigit()])
    input_path = "data/day" + day_num + ".txt"
    text_input = open(input_path, "r").read()

    print("1. Example : ", part1(example))
    print("1. Input : ", part1(text_input))

    print("-" * 100)

    print("2. Example : ", part2(example))
    print("2. Input : ", part2(text_input))

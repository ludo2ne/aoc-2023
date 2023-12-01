import os

example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

example2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def part1(text):
    lines = text.splitlines()
    total = 0

    for line in lines:
        for d in line:
            if d.isdigit():
                break
        for u in reversed(line):
            if u.isdigit():
                break
        total += int(d + u)

    return total


def part2(text):
    lines = text.splitlines()

    total = 0
    char_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for line in lines:
        for d in line:
            if d.isdigit():
                break
        d_index = line.index(d) if d.isdigit() else len(line)

        for u in reversed(line):
            if u.isdigit():
                break
        u_index = line.rindex(u) if u.isdigit() else 0

        first_index = len(line)
        last_index = 0

        for cd in char_digits:
            if cd in line[:d_index] and line[:d_index].index(cd) < first_index:
                first_index = line[:d_index].index(cd)
                d = char_digits[cd]
            if cd in line[u_index:] and line[u_index:].rindex(cd) > last_index:
                last_index = line[u_index:].rindex(cd)
                u = char_digits[cd]
        # print(f"{line:<50} {d}{u}")

        total += int(d + u)
    return total


if __name__ == "__main__":
    day_num = "".join([n for n in os.path.basename(__file__) if n.isdigit()])
    input_path = "data/day" + day_num + ".txt"
    text_input = open(input_path, "r").read()

    print("1. Example : ", part1(example))
    print("1. Input : ", part1(text_input))

    print("-" * 100)

    print("2. Example : ", part2(example2))
    print("2. Input : ", part2(text_input))

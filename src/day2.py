import os
from functools import reduce

example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def part1(text):
    lines = text.splitlines()
    color_max = {"red": 12, "green": 13, "blue": 14}

    total_id = 0

    for line in lines:
        id_game = int(line.split(":")[0][5:])
        valid_game = True

        for game in line.split(":")[1].split(";"):
            for cube in game.split(","):
                if int(cube.split()[0]) > color_max[cube.split()[1]]:
                    valid_game = False
        if valid_game:
            total_id += id_game

    return total_id


def part2(text):
    lines = text.splitlines()
    power = 0

    for line in lines:
        id_game = int(line.split(":")[0][5:])
        color_max = {"red": 1, "green": 1, "blue": 1}

        for game in line.split(":")[1].split(";"):
            for cube in game.split(","):
                if int(cube.split()[0]) > color_max[cube.split()[1]]:
                    color_max[cube.split()[1]] = int(cube.split()[0])

        power += reduce((lambda x, y: x * y), color_max.values())

    return power


if __name__ == "__main__":
    day_num = "".join([n for n in os.path.basename(__file__) if n.isdigit()])
    input_path = "data/day" + day_num + ".txt"
    text_input = open(input_path, "r").read()

    print("1. Example : ", part1(example))
    print("1. Input : ", part1(text_input))

    print("-" * 100)

    print("2. Example : ", part2(example))
    print("2. Input : ", part2(text_input))

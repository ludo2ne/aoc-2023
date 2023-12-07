import os

from time import time
from functools import cmp_to_key
from utils.get_input import import_input

example = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def get_hand_type(hand) -> str:
    cards = dict()
    res = None

    for c in hand:
        if c in cards:
            cards[c] += 1
        else:
            cards[c] = 1

    cards = sorted(cards.values(), reverse=True)

    if cards[0] == 5:
        res = "five"
    elif cards[0] == 4:
        res = "four"
    elif cards[0] == 3:
        if cards[1] == 2:
            res = "full"
        else:
            res = "three"
    elif cards[0] == 2:
        if cards[1] == 2:
            res = "2pairs"
        else:
            res = "pair"
    else:
        res = "high"

    return res

    # print(hand, res)


def compare_hands(h1, h2):
    h1_type = get_hand_type(h1)
    h2_type = get_hand_type(h2)
    # print(f"{h1} ({h1_type}) - {h2} ({h2_type})", end=" --> ")

    strength = {
        "five": 7,
        "four": 6,
        "full": 5,
        "three": 4,
        "2pairs": 3,
        "pair": 2,
        "high": 1,
    }

    values = dict([(str(i), i) for i in range(2, 10)])
    values["T"] = 10
    values["J"] = 11
    values["Q"] = 12
    values["K"] = 13
    values["A"] = 14

    if strength[h1_type] == strength[h2_type]:
        for i in range(len(h1)):
            if values[h1[i]] != values[h2[i]]:
                # print(values[h1[i]] > values[h2[i]])
                return 1 if values[h1[i]] > values[h2[i]] else -1
    else:
        # print(strength[h1_type] > strength[h2_type])
        return 1 if strength[h1_type] > strength[h2_type] else -1


def part1(text):
    lines = text.splitlines()

    total_winnings = 0
    hands_bid = dict((line.split() for line in lines))

    hands = [line.split()[0] for line in lines]

    for i, h in enumerate(sorted(hands, key=cmp_to_key(compare_hands))):
        # print(h, get_hand_type(h))
        total_winnings += (i + 1) * int(hands_bid[h])

    return total_winnings


def get_hand_type2(hand) -> str:
    cards = dict()
    res = None

    for c in hand:
        if c in cards:
            cards[c] += 1
        else:
            cards[c] = 1

    j = cards["J"] if "J" in cards else 0
    cards["J"] = 0

    cards = sorted(cards.values(), reverse=True)
    cards[0] += j

    if cards[0] == 5:
        res = "five"
    elif cards[0] == 4:
        res = "four"
    elif cards[0] == 3:
        if cards[1] == 2:
            res = "full"
        else:
            res = "three"
    elif cards[0] == 2:
        if cards[1] == 2:
            res = "2pairs"
        else:
            res = "pair"
    else:
        res = "high"

    # print(hand, res)

    return res


def compare_hands2(h1, h2):
    h1_type = get_hand_type2(h1)
    h2_type = get_hand_type2(h2)
    # print(f"{h1} ({h1_type}) - {h2} ({h2_type})", end=" --> ")

    strength = {
        "five": 7,
        "four": 6,
        "full": 5,
        "three": 4,
        "2pairs": 3,
        "pair": 2,
        "high": 1,
    }

    values = dict([(str(i), i) for i in range(2, 10)])
    values["T"] = 10
    values["J"] = 1
    values["Q"] = 12
    values["K"] = 13
    values["A"] = 14

    if strength[h1_type] == strength[h2_type]:
        for i in range(len(h1)):
            if values[h1[i]] != values[h2[i]]:
                # print(values[h1[i]] > values[h2[i]])
                return 1 if values[h1[i]] > values[h2[i]] else -1
    else:
        # print(strength[h1_type] > strength[h2_type])
        return 1 if strength[h1_type] > strength[h2_type] else -1


def part2(text):
    lines = text.splitlines()

    total_winnings = 0
    hands_bid = dict((line.split() for line in lines))

    hands = [line.split()[0] for line in lines]

    for i, h in enumerate(sorted(hands, key=cmp_to_key(compare_hands2))):
        # print(h, get_hand_type2(h))
        total_winnings += (i + 1) * int(hands_bid[h])

    return total_winnings


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

"""Third Day"""

from typing import Dict
from inputs import load_input


# PART 1


def calc_joltage1(bank: str) -> int:
    """Calculate the joltage of given battery bank"""
    digit1 = max(bank[:-1])
    index1 = bank.index(digit1)
    digit2 = max(bank[index1 + 1 :])

    return int(digit1 + digit2)


def part1(banks: list[str]) -> int:
    """Calculate and add joltages for each bank"""
    total = 0
    for bank in banks:
        total += calc_joltage1(bank)
    return total


#  Part 2


def calc_joltage2(bank: str) -> int:
    """Calculate joltage of given battery bank"""
    digits: Dict[int, int] = {n: -1 for n in range(12)}
    indices: Dict[int, int] = {n: -1 for n in range(12)}

    digits[0] = int(max(bank[:-11]))
    indices[0] = bank.index(str(digits[0]))

    for digitnum in range(1, 11):
        digits[digitnum] = int(max(bank[indices[digitnum - 1] + 1 : -(11 - digitnum)]))
        indices[digitnum] = (
            indices[digitnum - 1]
            + 1
            + int(bank[indices[digitnum - 1] + 1 :].index(str(digits[digitnum])))
        )  # .index(...) gives Index of the sliced list so the index before has to be added

    digits[11] = int(max(bank[indices[11 - 1] + 1 :]))

    total = ""
    for value in digits.values():
        total += str(value)

    return int(total)


def part2(banks: list[str]) -> int:
    """Calculate and add joltages for each bank"""
    total = 0
    for bank in banks:
        total += calc_joltage2(bank)
    return total


if __name__ == "__main__":
    INPUT = load_input(3).splitlines()
    print("Part 1")
    print(part1(INPUT))

    print("Part 2")
    print(part2(INPUT))

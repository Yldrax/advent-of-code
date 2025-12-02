"""First Day"""

from inputs import load_input


def part1(instructions: list[str]) -> int:
    """Turn dial and count occurances of zero"""
    total = 0
    dial = 50

    for instruction in instructions:
        mult = 1 if instruction[0] == "R" else -1
        step = int(instruction[1:])
        pointing = (dial + mult * step) % 100
        if pointing == 0:
            total += 1

    return total


def part2(instructions: list[str]) -> int:
    """Turn dial and count occurances of passing zero"""
    total = 0
    dial = 50

    for instruction in instructions:
        start = dial
        mult = 1 if instruction[0] == "R" else -1
        step = int(instruction[1:])
        passzero, dial = divmod(dial + mult * step, 100)

        total += abs(passzero)
        if start == 0 and mult == -1:
            total -= 1

    return total


def part2_force(instructions: list[str]) -> int:
    """Modulo doesnt work so here is the naive approach"""
    total = 0
    dial = 50

    for instruction in instructions:
        mult = 1 if instruction[0] == "R" else -1
        value = int(instruction[1:])

        while value > 0:
            dial = dial + mult
            value -= 1

            if dial == -1:
                dial = 99
            elif dial == 100:
                dial = 0

            if dial == 0:
                total += 1

    return total


if __name__ == "__main__":
    INPUT = load_input(1).splitlines()

    print("Part 1: ")
    print(part1(INPUT))

    print("Part 2:")
    print(part2(INPUT))
    print(part2_force(INPUT))

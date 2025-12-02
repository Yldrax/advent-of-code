"""Second Day"""

from inputs import load_input


# PART 1
def is_valid_1(id: int) -> bool:
    """Check if ID is valid - invalid if any pattern repeated 2 times"""
    idstring = str(id)

    if idstring[: len(idstring) // 2] == idstring[len(idstring) // 2 :]:
        return False

    return True


def part1(idranges: list[list[int]]) -> int:
    "Check ID ranges for invalid IDs"
    total = 0

    for idrange in idranges:
        for i in range(idrange[0], idrange[1] + 1):
            total = total + i if not is_valid_1(i) else total

    return total


# PART 2
def get_divisors(n: int) -> list[int]:
    """Get divisors of a number (slow naive approach)"""
    divisors = []

    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors


def is_valid_2(id: int) -> bool:
    """Check if ID is valid - invalid if any pattern repeated at least 2 times"""
    idstring = str(id)
    partsizes = get_divisors(len(idstring))

    for partsize in partsizes:
        split_id = [
            idstring[i : i + partsize] for i in range(0, len(idstring), partsize)
        ]
        if len(set(split_id)) == 1:
            return False

    return True


def part2(idranges: list[list[int]]) -> int:
    "Check ID ranges for invalid IDs"
    total = 0

    for idrange in idranges:
        for i in range(idrange[0], idrange[1] + 1):
            total = total + i if not is_valid_2(i) else total

    return total


if __name__ == "__main__":
    INPUT = [[int(n) for n in m.split("-")] for m in load_input(2).strip().split(",")]
    print("Part 1:")
    print(part1(INPUT))
    print("Part 2:")
    print(part2(INPUT))

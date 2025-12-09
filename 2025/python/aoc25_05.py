"""Fifth Day"""

from inputs import load_input


# Part 1
def part1(freshranges: list[tuple[int, int]], ingredients: list[int]) -> int:
    """Count fresh ingredients"""
    fresh_total = 0

    for ingredient in ingredients:
        for freshrange in freshranges:
            if freshrange[0] <= ingredient <= freshrange[1]:
                fresh_total += 1
                break

    return fresh_total


# Part 2
def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping ranges"""
    sorted_ranges = sorted(ranges)

    change = True
    while change:
        change = False
        new_ranges = []
        for i, cur_range in enumerate(sorted_ranges[:-1]):
            if cur_range[1] >= sorted_ranges[i + 1][0]:
                change = True
                new_ranges.append(
                    (cur_range[0], max(sorted_ranges[i + 1][1], cur_range[1]))
                )
                new_ranges = new_ranges + sorted_ranges[i + 2 :]
                sorted_ranges = new_ranges
                break
            new_ranges.append(cur_range)

    return sorted_ranges


def part2(freshranges: list[tuple[int, int]]) -> int:
    """Count total ingredient IDs contained in the ranges"""
    total_fresh = 0

    merged_ranges = merge_ranges(freshranges)
    for ing_range in merged_ranges:
        total_fresh += ing_range[1] - ing_range[0] + 1

    return total_fresh


if __name__ == "__main__":
    INPUT = load_input(5)
    INPUT1 = [
        tuple(map(int, line.split("-"))) for line in INPUT.split("\n\n")[0].splitlines()
    ]
    INPUT2 = [int(n) for n in INPUT.split("\n\n")[1].splitlines()]

    print("Part 1")
    print(part1(INPUT1, INPUT2))

    print("Part 2")
    print(part2(INPUT1))

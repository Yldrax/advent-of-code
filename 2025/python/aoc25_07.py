"""Seventh Day"""

from inputs import load_input


def part1(manifold: list[list[str]]) -> int:
    """Simulate tachyon beam and count the splits"""
    splits = 0
    manifold[1][len(manifold[0]) // 2] = "|"

    for y in range(1, len(manifold)):
        for x in range(len(manifold[0])):
            if manifold[y - 1][x] == "|":
                if manifold[y][x] == ".":
                    manifold[y][x] = "|"
                if manifold[y][x] == "^":
                    splits += 1
                    manifold[y][x - 1] = "|"
                    manifold[y][x + 1] = "|"

    return splits


if __name__ == "__main__":
    INPUT1 = [list(line) for line in load_input(7).splitlines()]
    print(part1(INPUT1))

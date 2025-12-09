"""Fourth Day"""

from inputs import load_input


def part1(rollmap: list[list[str]]) -> int:
    """Calculate number of accesible rolls"""
    total = 0
    height = len(rollmap)
    width = len(rollmap[0])

    for y, row in enumerate(rollmap):
        for x, roll in enumerate(row):
            if roll == "@":
                neighbours = 0
                offsets = [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]
                for dy, dx in offsets:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width:
                        neighbours += 1 if rollmap[ny][nx] == "@" else 0
                if neighbours < 4:
                    total += 1

    return total


def part2(rollmap: list[list[str]]) -> int:
    "Calculate number of accessible rolls with removal of accesible rolls in the way"
    total = 0
    height = len(rollmap)
    width = len(rollmap[0])
    change = True

    while change:
        change = False
        for y, row in enumerate(rollmap):
            for x, roll in enumerate(row):
                if roll == "@":
                    neighbours = 0
                    offsets = [
                        (-1, -1),
                        (-1, 0),
                        (-1, 1),
                        (0, -1),
                        (0, 1),
                        (1, -1),
                        (1, 0),
                        (1, 1),
                    ]
                    for dy, dx in offsets:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < height and 0 <= nx < width:
                            neighbours += 1 if rollmap[ny][nx] == "@" else 0
                    if neighbours < 4:
                        total += 1
                        rollmap[y][x] = "."
                        change = True

    return total


if __name__ == "__main__":
    INPUT = [list(line) for line in load_input(4).splitlines()]
    print("Part 1")
    print(part1(INPUT))

    print("Part 2")
    print(part2(INPUT))

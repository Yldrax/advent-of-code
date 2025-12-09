"""Fourth Day"""

from inputs import load_input


def part1(rollmap: list[list[str]]) -> int:
    total = 0

    for y, row in enumerate(rollmap):
        for x, roll in enumerate(row):
            if roll == "@":
                neighbours = 0
                offsets = [
                    (1, -1),
                    (1, 0),
                    (1, 1),
                    (0, -1),
                    (0, 1),
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                ]
                for offset in offsets:
                    try:
                        neighbours = (
                            neighbours + 1
                            if rollmap[y + offset[0]][x + offset[1]] == "@"
                            else neighbours
                        )
                        print(f"coords:{(x, y)}, nc = {(x, y) + offset}")
                    except IndexError:
                        pass
                print(neighbours)
                if neighbours < 4:
                    total += 1

    return total


if __name__ == "__main__":
    INPUT = [list(line) for line in load_input(4).splitlines()]
    #       print(part1(INPUT))

    test = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
    test = [list(line) for line in test.splitlines()]
    print(part1(test))

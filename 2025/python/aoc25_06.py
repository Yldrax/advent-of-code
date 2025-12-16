"""Sixth Day"""

import re
from inputs import load_input


def part1(homework: list[list[str]]) -> int:
    """Do homework according to cephalopod math"""
    total = 0
    for a, b, c, d, x in zip(*homework):
        match x:
            case "+":
                total += int(a) + int(b) + int(c) + int(d)
            case "*":
                total += int(a) * int(b) * int(c) * int(d)

    return total


def part2(homework: list[str]) -> int:
    """Do homework according to real cephalopod math """
    total = 0
    count = 1
    n1, n2, n3, n4 = -1, -1, -1, -1

    for a, b, c, d, x in zip(*(reversed(col) for col in homework)):
        match count:
            case 1:
                n1 = int((a + b + c + d).strip())
            case 2:
                n2 = int((a + b + c + d).strip())
            case 3:
                n3 = int((a + b + c + d).strip())
            case 4:
                n4 = int((a + b + c + d).strip())
        count += 1

        match x:
            case "+":
                n1 = 0 if n1 == -1 else n1
                n2 = 0 if n2 == -1 else n2
                n3 = 0 if n3 == -1 else n3
                n4 = 0 if n4 == -1 else n4
                total += n1 + n2 + n3 + n4
                count = 0
                n1,n2,n3,n4 = -1,-1,-1,-1
            case "*":
                n1 = 1 if n1 == -1 else n1
                n2 = 1 if n2 == -1 else n2
                n3 = 1 if n3 == -1 else n3
                n4 = 1 if n4 == -1 else n4
                total += n1 * n2 * n3 * n4
                count = 0
                n1,n2,n3,n4 = -1,-1,-1,-1

    return total


if __name__ == "__main__":
    INPUT1 = [re.findall(r"\S+", x) for x in load_input(6).splitlines()]
    print("Part 1")
    print(part1(INPUT1))

    print("Part 2")
    INPUT2 = load_input(6).splitlines()
    print(part2(INPUT2))

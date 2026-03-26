"""
Possible solution to Advent of Code 2015 Day 6.
https://adventofcode.com/2015/day/6
"""
from unittest import case


def gimme_data():
    with open("dataset.txt") as file:
        return [line.strip().replace("through ", '').replace("turn on", '1').replace("turn off", '2').replace("toggle", '3') for line in file]


def solve(data: list[str]) -> tuple[int, int]:
    result_part1 = _part_1(data)
    result_part2 = _part_2(data)

    return result_part1, result_part2

def _part_1(data: list[str]) -> int:
    lights = dict()

    for instruction in data:
        scenario, start, end = instruction.split(" ")
        match scenario:
            case '1':
                for x in range(int(start)):
                    for y in range(int(end) + 1):
                        lights[(x, y)] = 1
            case '2':
                for x in range(int(start)):
                    for y in range(int(end) + 1):
                        lights[(x, y)] = 0
            case '3':
                for x in range(int(start)):
                    for y in range(int(end) + 1):
                        lights[(x, y)] = 1 if lights[(x, y)] == 0 else 0

    return sum(lights)


def _part_2(data: list[str]) -> int:
    return 0


def main():
    data = gimme_data()

    result = solve(data)

    print(f"The solution is to part 1 is: {result[0]}")
    print(f"The solution is to part 2 is: {result[1]}")

if __name__ == "__main__":
    main()

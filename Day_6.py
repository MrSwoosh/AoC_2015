"""
Possible solution to Advent of Code 2015 Day 6.
https://adventofcode.com/2015/day/6
"""
import sys

def gimme_data() -> list[str]:
    try:
        with open("dataset.txt") as file:
            return [line.strip().replace("through ", '').replace("turn on", '1')
                    .replace("turn off", '2').replace("toggle", '3') for line in file]
    except FileNotFoundError:
        print("File not found.")
        print("There is no point in continuing without some data.")
        print("Exiting...")
        sys.exit(1)


def solve(data: list[str]) -> tuple[int, int]:
    result_part1 = _part_1(data)
    result_part2 = _part_2(data)

    return result_part1, result_part2


def _part_1(data: list[str]) -> int:
    lights = dict()

    for instruction in data:
        scenario, start, end = instruction.split(" ")
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        match scenario:
            case '1':
                for x in range(int(x1), int(x2) + 1):
                    for y in range(int(y1), int(y2) + 1):
                        lights[(x, y)] = 1
            case '2':
                for x in range(int(x1), int(x2) + 1):
                    for y in range(int(y1), int(y2) + 1):
                        lights[(x, y)] = 0
            case '3':
                for x in range(int(x1), int(x2) + 1):
                    for y in range(int(y1), int(y2) + 1):
                        if (x, y) not in lights:
                            lights[(x, y)] = 1
                        else:
                            lights[(x, y)] = 1 if lights[(x, y)] == 0 else 0

    return sum(lights.values())


def _part_2(data: list[str]) -> int:
    lights_2 = dict()

    for instruction in data:
        scenario, start, end = instruction.split(" ")
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        match scenario:
            case '1':
                for x in range(int(x1), int(x2) + 1):
                    for y in range(int(y1), int(y2) + 1):
                        if (x, y) not in lights_2:
                            lights_2[(x, y)] = 0
                        lights_2[(x, y)] += 1
            case '2':
                for x in range(int(x1), int(x2) + 1):
                    for y in range(int(y1), int(y2) + 1):
                        if (x, y) not in lights_2:
                            lights_2[(x, y)] = 0
                        lights_2[(x, y)] = max(0, lights_2[(x, y)] -1)
            case '3':
                for x in range(int(x1), int(x2) + 1):
                    for y in range(int(y1), int(y2) + 1):
                        if (x, y) not in lights_2:
                            lights_2[(x, y)] = 2
                        else:
                            lights_2[(x, y)] += 2

    return sum(lights_2.values())


def main():
    data = gimme_data()

    result = solve(data)

    print(f"The solution is to part 1 is: {result[0]}")
    print(f"The solution is to part 2 is: {result[1]}")


if __name__ == "__main__":
    main()

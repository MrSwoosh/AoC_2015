"""
Possible solution to Advent of Code 2015 Day 6.
https://adventofcode.com/2015/day/6

Imagine a 1000*1000 grid where every element represents a light.
Part 1
    Every light can be turned on, off or toggled.
Part 2
    Every light has a state representing its brightness.

The algorithm doesn't use an actual grid. It stores the x, y position
as a tuple in a dictionary. This reduces memory usage by not storing
values for unused positions. Only efficient when not all positions are used.
Instructions don't require searching in a grid, which could make a 2D grid
a more efficient option. But this will require to manually search for grid
limits in the input data, built in a method to determine size,
 or resize grid during processing. I don't like either options,
 making me prefer the dictionary approach.

Time complexity
gimme_data(): O(n)
solve(): O(2n)
_part_1(): for every instruction O(k) where k = surface of rectangle -> O(n * k) == O(n * grid size)
_part_2(): for every instruction O(k) where k = surface of rectangle -> O(n * k) == O(n * grid size)

Possible improvements
-   _part_1() and _part_1() each iterate over the dataset.
    Can be merged to 1 method to reduce iterations from 2 to 1,
    but will diminish readability.
-   Memory usage can be reduced further by removing a position
    from the dictionary when its value is 0.
-   Number of dictionary look-up is high.
    Could be reduced by using lights[(x, y)] = lights.get((x, y), 0) + 1
"""

import sys

def gimme_data() -> list[str]:
    """
    Retrieves data from a file, for the algorithm to process.
    Transforms lines for easier processing.
        "turn on" -> '1'
        "turn off" -> '2'
        "toggle" -> "3"
        remove "through"
    Example:
        "toggle 461,550 through 564,900" -> "3 461,550 564,900"

    :return: List with transformed strings.
    """
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
    """
    Handles solving each part individually.

    :param data: List with instructions. (list[str])
    :return: tuple with 2 ints, representing the solutions to part 1 and 2. (tuple[int, int])
    """
    result_part1 = _part_1(data)
    result_part2 = _part_2(data)

    return result_part1, result_part2


def _part_1(data: list[str]) -> int:
    """
    Processes instructions to find the solution to part 1.
    The first character of every instruction sets the scenario.
        1: turn on - set position state to 1, regardless of its state.
        2: turn off - set position state to 0, regardless of its state.
        3: toggle - set position state to 1 if current state is 0, or 0 if current state is 1.

    :param data: List with instructions. (list[str])
    :return: sum of lights that are on. (int)
    """
    lights = dict()

    for instruction in data:
        scenario, start, end = instruction.split(" ")
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        match scenario:
            case '1':
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        lights[(x, y)] = 1
            case '2':
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        lights[(x, y)] = 0
            case '3':
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        if (x, y) not in lights:
                            lights[(x, y)] = 1
                        else:
                            lights[(x, y)] = 1 if lights[(x, y)] == 0 else 0

    return sum(lights.values())


def _part_2(data: list[str]) -> int:
    """
        Processes instructions to find the solution to part 2.
        Uses the same logic as _part_1(), but with different values.
        The first character of every instruction sets the scenario.
            1: turn on - increase the value of the position by 1.
            2: turn off - decrease the value of the position by 1. Lowest value is 0.
            3: toggle - increase the value of the position by 2.

        :param data: List with instructions. (list[str])
        :return: sum of lights that are on. (int)
        """
    lights_2 = dict()

    for instruction in data:
        scenario, start, end = instruction.split(" ")
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        match scenario:
            case '1':
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        if (x, y) not in lights_2:
                            lights_2[(x, y)] = 0
                        lights_2[(x, y)] += 1
            case '2':
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        if (x, y) not in lights_2:
                            lights_2[(x, y)] = 0
                        lights_2[(x, y)] = max(0, lights_2[(x, y)] -1)
            case '3':
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
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

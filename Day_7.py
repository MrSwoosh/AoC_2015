"""
Possible solution to Advent of Code 2015 Day 7.
https://adventofcode.com/2015/day/7

Part 1 recursion

Time complexity

Possible improvements
"""

import sys


def gimme_them_data() -> dict[str, list[str]]:
    """
    Retrieves data from input file.
    Calls _uniform_syntax() to transform input to an output with uniform syntax.
    Transforms the operator in the instruction to a number for easier processing.
    Example:
        input               ->      output
        "jx AND jz -> ka"   ->      data["ka"]  =   ["jx" '3' "jz"]
        "NOT im -> in"      ->      data["in"]  =   ['', '0', "im"]
        "lx -> a"           ->      data["a"]   =   ['', '5', "lx"]
    :return: a dictionary with the keys representing destinations,
    and values (list) representing the instructions
    """
    data = dict()
    shorthand = {"NOT":     '0',
                 "LSHIFT":  '1',
                 "RSHIFT":  '2',
                 "AND":     '3',
                 "OR":      '4',
                 "COPY":    '5'}

    try:
        with open("dataset.txt") as file:
            for row in file:
                row = row.strip()
                instruction, destination = row.split(" -> ")

                instruction_parts = _uniform_syntax(instruction)  # transform syntax

                instruction_parts[1] = shorthand[instruction_parts[1]]  # transform operator

                data[destination] = instruction_parts
    except FileNotFoundError:
        print("File not found.")
        print("There is no point in continuing without some data.")
        print("Exiting...")
        sys.exit(1)

    return data


def _uniform_syntax(instruction: str) -> list[str]:
    """

    :param instruction:
    :return:
    """
    instruction_parts = instruction.split(' ')  # transform str into list: "iw AND ix" -> ["iw", "AND", "ix"]
    if len(instruction_parts) == 1:  # add operator to assignment instruction: ['x'] -> ["COPY", 'x']
        instruction_parts.insert(0, "COPY")
    if len(instruction_parts) == 2:  # transform instruction to uniform syntax: ["NOT", 'b'] -> ["", "NOT", 'b']
        instruction_parts.insert(0, "")

    return instruction_parts


def solve(instructions: dict[str, list[str]]) -> tuple[int, int]:
    starting_point = 'a'
    result_part1 = _part_1(starting_point, instructions)
    result_part2 = _part_2()

    return result_part1, result_part2


def _part_1(start, instructions) -> int:
    """

    :param start:
    :param instructions:
    :return:
    """
    return 0


def _part_2() -> int:
    return 0


def main():
    data = gimme_them_data()

    result = solve(data)

    print(f"The value of wire a and therefore the solution is to part 1 is: {result[0]}")
    print(f"The solution is to part 2 is: {result[1]}")


if __name__ == "__main__":
    main()

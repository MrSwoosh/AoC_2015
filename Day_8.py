"""
Possible solutions to Advent of Code 2015 Day 8
https://adventofcode.com/2015/day/8
"""


import sys


def fetch_data():
    try:
        with open("dataset.txt") as file:
            return [string.strip() for string in file]
    except FileNotFoundError:
        print("Something went wrong while locating de dataset.")
        print("Please check it and try again.")
        sys.exit(1)


def solve(data):
    result_part_1 = _part_1(data)
    result_part_2 = _part_2(data)

    return result_part_1, result_part_2

def _part_1(data):
    total_characters = 0
    in_mem_characters = 0

    for string in data:
        total_characters += len(string)

        position = 0
        while position < len(string) - 1:
            match string[position]:
                case '"':
                    pass
                case '\\':
                    if string[position + 1] == "\\" or string[position + 1] == "\"":
                        position += 1
                    else:
                        position += 3
                    in_mem_characters += 1
                case _:
                    in_mem_characters += 1

            position += 1

    return total_characters - in_mem_characters


def _part_2(data):
    return 0


def main():
    data = fetch_data()

    answers = solve(data)

    print(f"The answer to day 8 part 1: {answers[0]}")
    print(f"The answer to day 8 part 2: {answers[1]}")

if __name__ == "__main__":
    main()

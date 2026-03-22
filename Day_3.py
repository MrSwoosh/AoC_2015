"""
Possible solution for Advent of Code 2016 Day 3
https://adventofcode.com/2015/day/3

Solving it all in 1 O(n) function
No OOP, no type annotations, no detailed documentation,
just some lazy coding with one hand,
because my cat claimed the other one.
"""

import sys


def main():
    # Variables part 1
    santa_part_1 = [0, 0]
    seen_part_1 = {(0, 0)}

    # variables part 2
    santa_part_2 = [0, 0]
    robo_santa = [0, 0]
    seen_part_2 = {(0, 0)}

    direction = {'^': (1, 0),
                 'v': (-1, 0),
                 '<': (0, -1),
                 '>': (0, 1)}

    try:
        with open("dataset_3.txt") as file:
            instructions = file.read().strip()
    except FileNotFoundError:
        print("Something went wrong opening the input file.\n"
              "Check it and try again.")
        sys.exit(1)

    for i, char in enumerate(instructions):
        # Check validity of character
        if char not in direction:
            print("Illegal character found in instructions.\n"
                  "Closing program.")
            sys.exit(1)

        # Switch between santa and robot santa for part 2
        current = santa_part_2 if i % 2 == 0 else robo_santa

        # Adjust positions for both parts
        dx, dy = direction[char]
        santa_part_1[0] += dx
        santa_part_1[1] += dy
        current[0] += dx
        current[1] += dy

        # Store positions
        seen_part_1.add(tuple(santa_part_1))
        seen_part_2.add(tuple(current))

    # Print solutions
    print(f"The number of houses that receive a present for part 1 is: {len(seen_part_1)}.")
    print(f"The number of houses that receive a present for part 2 is: {len(seen_part_2)}.")


if __name__ == "__main__":
    main()

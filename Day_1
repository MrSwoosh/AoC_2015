"""
Possible solution for Advent of Code 2015.
https://adventofcode.com/2016/day/1

Part 1 iterates twice over the input by using _counter(), for practice purposes.
Can be done in 1 iteration with: sum(1 if c == '(' else -1 for c in roadmap)

Complexity part 1: O(2n)
    Can be O(n) by using .count() instead of ._counter()
Complexity part 2: O(n)
"""

import sys


class DataHandler:
    """
    Class to handle all data ETL processes.
    """

    def give_me_data(self) -> str:
        """
        Loads data from input file.

        :return: a stripped string from input file.
        """
        try:
            with open("dataset_1.txt") as file:
                return file.readline().strip()
        except FileNotFoundError:
            print("Something went wrong opening the input file.\n"
                  "Check it and try again.")
            sys.exit(1)


class Processor:
    """
    Handles all processing needed to find the answers.
    """

    def process_complete_roadmap(self, roadmap: str) -> int:
        """
        None of the helper method calls are needed, but are
        used to practice correct coding methodologies and conventions.
        :roadmap: Sequence of instructions.
        :return: final floor value after processing.
        """
        up = self._counter(roadmap, '(')
        down = self._counter(roadmap, ')')
        final_floor = self._calculate(up, down)

        return final_floor

    def _counter(self, road: str, char: str) -> int:
        """
        Helper that counts the number of times a char appears in a string.

        Method is over-engineered, but useful to practice coding.

        :road: string containing chars.
        :char: char to count in road.
        :return: the number of times the char appears in the string.
        """
        number = road.count(char)

        return number

    def _calculate(self, up: int, down: int) -> int:
        """
        Calculates the final floor by subtracting the number of times
        Santa goes down a floor, from the number of times Santa
        moves up a floor.

        :up: integer value for the number of times Santa moves up a floor.
        :down: integer value for the number of times Santa moves down a floor.
        :return: final floor value.
        """
        result = up - down  # Can and should be shorter, but we're practicing.

        return result

    def basement_boogy(self, roadmap: str) -> int:
        """
        Processes every instruction in the roadmap,
        up to the point the floor becomes negative.

        match/case is over-engineered for these instructions,
        but useful to practice coding.

        :roadmap: sequence of instructions.
        :return: the number of instructions processed before Santa reaches the basement.
        """
        floor_switches = 0
        current_floor = 0
        for instruction in roadmap:
            # Running prefix sum

            match instruction:
                case '(':
                    current_floor += 1
                case ')':
                    current_floor -= 1
                case _:
                    print("Something went wrong while processing the instructions.\n"
                          "Check the code, and try again.")
                    sys.exit(1)

            floor_switches += 1

            if current_floor < 0:
                return floor_switches

        print("Santa never reached the basement.\n"
              "Should this be possible?")
        return -1


def main():
    datahandler = DataHandler()
    data = datahandler.give_me_data()
    processor = Processor()

    result_part_1 = processor.process_complete_roadmap(data)
    print(f"After a long walk, Santa arrives at floor {result_part_1}.")

    result_part_2 = processor.basement_boogy(data)
    print(f"After visiting several floors, Santa finds himself in the basement after {result_part_2} floors.")


if __name__ == "__main__":
    main()

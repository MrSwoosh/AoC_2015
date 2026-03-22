"""
Possible solution to Advent of Code 2015 day 2.
https://adventofcode.com/2015/day/2
Date: 15-3-2026

Classes are overengineering,
but fine to practice OOP.
"""


class Datahandler:
    """
    Handles ETL
    """

    @staticmethod
    def get_data(location: str) -> list[list[int]]:
        """
        Loads data from input file.
        Transforms data to list of integers

        :param location: file name for target input file
        :return: list of lists with sorted integers
        """
        with open(location) as file:
            return [sorted(int(x) for x in row.split('x')) for row in file]


class Dataprocessor:

    @staticmethod
    def solve_parts(box_dimensions: list[list[int]]) -> tuple[int, int]:
        """
        Part 1: calculates square footage of all present sides,
        plus the footage of the smallest side.
        Part 2: calculates the length of ribbon needed.
        ribbon has 2 parts; box and bow
        bow is equal to l*w*h
        box is equal to 2 * smallest value + 2 * second smallest value
        ribbon length = bow + box

        :param box_dimensions: list of present sizes, int
        :return: tuple of integers, representing the solutions to part 1 and 2
        """
        paper_needed = 0
        ribbon_needed = 0
        for l, w, h in box_dimensions:
            a = l * w
            b = l * h
            c = w * h

            # Square footage of all sides = 2*l*w + 2*l*h + 2*w*h
            paper_needed += 2 * (a + b + c) + min(a, b, c)  # 2*l*w + 2*l*h + 2*w*h == 2(l*w + l*h + w*h)

            # smallest + smallest + second smallest + second smallest + l*w*h
            ribbon_needed += 2 * l + 2 * w + a * h  # _[0] * _[1] has already been calculated in a

        return paper_needed, ribbon_needed


def main():
    # Set scenario to True of False
    test = False
    # Set target file location
    file_location = "test_input" if test else "dataset_2"
    # Retrieve data
    data_set = Datahandler.get_data(file_location)

    # Solve parts of puzzle
    result_part_1, result_part_2 = Dataprocessor.solve_parts(data_set)
    print(f"Answer to part 1: {result_part_1}")
    print(f"Answer to part 2: {result_part_2}")


if __name__ == "__main__":
    main()

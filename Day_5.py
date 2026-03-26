"""
Possible solution for Advent of Code 2015 Day 5.
https://adventofcode.com/2015/day/5

The solution to part 2 uses a set to keep track of combinations.
The .count() method would also work, but is inefficient,
because it would iterate over the whole string for every pair.
Resulting in len(string) -1 iterations for every string.

Timecomplexity:
gimme_data(): O(n)
_part_1(): O(m)
_part_2(): O(m)
solve_parts(): O(n * m)

Suggestions for improvements:
_part_2() logic could be more efficient.
"""

def gimme_data() -> list[str]:
    """
    Retrieves data from input file.
    Stores lines in list.
    :return: List of lines from input file.
    """
    data = list()

    with open("dataset.txt") as file:
        return [line.strip() for line in file]


def solve_parts(data: list[str]) -> tuple[int, int]:
    """
    Outsources the tasks to helper methods, just like Santa
    does with his elves.
    :param data: List of strings to be evaluated.
    :return: Integers representing the number of nice strings,
    according to the requirements for both parts of the puzzle.
    """
    number_nice_strings_part_1 = 0
    number_nice_strings_part_2 = 0

    for string in data:
        number_nice_strings_part_1 += 1 if _part_1(string) else 0
        number_nice_strings_part_2 += 1 if _part_2(string) else 0

    return number_nice_strings_part_1, number_nice_strings_part_2


def _part_1(string: str) -> bool:
    """
    Checks whether string is nice string or not.
    Requirements:
        String contains at least 3 vowels (aeiou)
        String contains at least 1 pair of equal letters (aa, bb, ...)
        String does not contain "ab", "cd", "pq" or "xy".
    :param string: String to be evaluated.
    :return: Boolean value indicating whether string is nice or not.
    """
    number_vowels = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    contains_equal_pair = False
    naughty_pairs = {"ab", "cd", "pq", "xy"}

    for i, char in enumerate(string):
        # Check if char is a vowel
        if number_vowels < 3 and char in vowels:  # pruning checks once requirement is satisfied
            number_vowels += 1

        # Check pairs
        if i != 0:
            pair = string[i-1:i+1]
            # Check if pair consists of 2 equal letters
            if not contains_equal_pair and pair[0] == pair[1]:  # pruning checks once requirement is satisfied
                contains_equal_pair = True
            # Check if pair is naughty
            if pair in naughty_pairs:  # End evaluation if string contains a naughty pair
                return False

    return number_vowels == 3 and contains_equal_pair


def _part_2(string: str) -> bool:
    """
    Checks whether string is nice string or not.
    Requirements:
        A string contains at least 2 equal pairs of equal letters.
        A string contains at least 1 group of 3, with the pattern xyx ("aba", "nmn", ...).
    :param string: String to be evaluated.
    :return: Boolean value indicating whether string is nice or not.
    """
    xyx = False  # state for presence of xyx format
    pairs = set()  # store seen pairs
    two_pair = False  # state for presence of 2 identical pairs
    pairs.add(string[:2])  # add first pair to make logic easy to follow

    for i in range(2, len(string)):
        if not xyx:  # prune
            # Check for xyx format
            if string[i-2] == string[i]:
                if string[i-1] != string[i]:
                    xyx = True

        if not two_pair:  # prune
            # Check for format xyyy, if true -> move on
            if string[i-1] == string[i]:
                if string[i-2] == string[i-1] and (i-3 < 0 or string[i-3] != string[i-2]):
                    continue

            # Check if pair has already been seen
            if string[i-1:i+1] in pairs:
                two_pair = True
            else:
                pairs.add(string[i-1:i+1])

    return xyx and two_pair


def main():
    data = gimme_data()  # retrieve data

    result = solve_parts(data)  # solve the challenge

    # present results
    print(f"The number of nice strings according to the requirements of part 1: {result[0]}")
    print(f"The number of nice strings according to the requirements of part 2: {result[1]}")


if __name__ == '__main__':
    main()

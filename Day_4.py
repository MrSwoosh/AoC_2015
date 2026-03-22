"""
Possible solution for Advent of Code 2015 Day 4.
https://adventofcode.com/2015/day/4

This script searches for the lowest integer that, when appended to a given key
and hashed with MD5, produces a hash starting with a given number of leading zeros.
"""

import hashlib


def find_number(number: int, size: int, key: str) -> int:
    """
    Finds the lowest integer greater than or equal to `number` such that
    the MD5 hash of (key + number) starts with `size` leading zeroes.

    Method contract:
    - `number` must be a non-negative integer.
    - `size` must be a positive integer.
    - `key` must be a non-empty string.
    - The function will always return an integer >= `number`.

    :param number: The starting number for the search (inclusive). (int)
    :param size: The number of leading zeroes required in the hash. (int)
    :param key: The secret key used as prefix for hashing. (str)
    :return: The first integer for which the hash meets the condition. (int)

    Notes:
        - This function performs a brute-force search and may take time
          for larger values of `size`. For a small dataset, which AoC usually has,
          and a low level challenge, brute force is fine.
        - Uses MD5 hashing via the hashlib library.
    """
    pattern = '0' * size

    while True:
        hash_result = hashlib.md5((key + str(number)).encode()).hexdigest()

        if hash_result[:size] == pattern:
            return number
        else:
            number += 1


def main() -> None:
    """
    Entry point of the script.

    Solves both parts of the puzzle:
    - Part 1: Find a number that produces a hash with 5 leading zeroes.
    - Part 2: Continue searching for a hash with 6 leading zeroes.

    Method contract:
    - No input arguments required.
    - Prints results directly to console.

    Notes:
        - Part 2 continues searching from the result of Part 1 for efficiency.
    """

    seed = "ckczppom"
    number_part1 = find_number(0, 5, seed)
    number_part2 = find_number(number_part1, 6, seed)

    print(f"Result part 1 = {number_part1}")
    print(f"Result part 2 = {number_part2}")


if __name__ == '__main__':
    main()

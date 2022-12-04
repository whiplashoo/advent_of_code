# aoc.py
import re
from typing import List


def input_as_string(filename: str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")


def input_as_lines(filename: str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")


def input_as_ints(filename: str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    def line_as_int(l): return int(l.rstrip('\n'))
    return list(map(line_as_int, lines))


def print_matrix(matrix):
    for row in matrix:
        print(" ".join([str(x) for x in row]))


def parse_ints_str(line: str) -> List[int]:
    return [int(x) for x in re.findall(r'[\+\-]?[0-9]+', line)]

"""
You start on the open square (.) in the top-left corner and 
need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes 
(you opted for a cheaper model that prefers rational numbers); start by 
counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 
and down 1. Then, check the position that is right 3 and down 1 from there, and so 
on until you go past the bottom of the map.
"""

from __future__ import annotations
from typing import List, NamedTuple, Tuple, Set
import itertools
from collections import defaultdict, Counter

RAW = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


Point = Tuple[int, int]

class Slope(NamedTuple):
    trees: List[Point]
    width: int
    height: int

    @staticmethod
    def parse(raw: str) -> Slope:
        Lines = raw.split("\n")
        trees = {
            (x, y)
            for y, row in enumerate(Lines)
            for x, c in enumerate(row.strip())
            if c == '#'
        }

        width = len(Lines[0])
        height = len(Lines)

        return Slope(trees, width, height)

SLOPE = Slope.parse(RAW)


def count_tree(
    slope: Slope,
    right: int = 3,
    down: int = 1
) -> int:
    num_trees = 0
    x = 0
    for y in range(0, slope.height, down):
        #print(x, y)
        if (x, y) in slope.trees:
            num_trees += 1
        x = (x + right) % slope.width
    return num_trees


assert  count_tree(SLOPE) == 7

with open("inputs/day03_input.txt") as f:
    row = f.read()
slope = Slope.parse(row)
print(count_tree(slope))



# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2


def trees_product(slope: Slope, slopes: List[Point]) -> int:
    product = 1
    for right, down in slopes:
        product *= count_tree(slope, right=right, down=down)

    return product


SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

assert trees_product(SLOPE, SLOPES) == 336

print(trees_product(slope, SLOPES))

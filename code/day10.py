"""https://adventofcode.com/2020/day/10"""
##
## advent of code Day10
##

# Import libraries
from typing import List
from collections import Counter


class Adapter:
    def __init__(self, output: str) -> None:
        self.output = output

    def parse(self) -> list[int]:
        return [
            int(out)
            for out in self.output.split("\n")
        ]

    def jolt(self) -> Counter:

        # List of output jolts: output_jolts
        output_jolts = self.parse()

        output_jolts.append(max(output_jolts) + 3)
        output_jolts.insert(0, 0)

        # Sorting the output jolt to descending order
        output_jolts.sort(reverse=True)

        # Initial the index and jolt_length
        index = 0
        next_index = 1
        jolt_length = len(output_jolts)
        ratings = []

        while index < jolt_length:
            if next_index == jolt_length:
                break
            ratings.append(output_jolts[index] - output_jolts[next_index])
            index += 1
            next_index += 1

        return Counter(ratings)

    def multipier(self) -> int:
        # Get the values from the jolt function: jolt_values
        jolt_values = list(self.jolt().values())

        # Number of ratings of jolt: one_rating_jolt, three_rating_jolt
        one_rating_jolt = jolt_values[0]
        three_rating_jolt = jolt_values[1]
        return one_rating_jolt * three_rating_jolt

    def count_paths(self) -> int:
        adapters = self.parse()
        adapters.append(0)
        adapters.append(max(adapters) + 3)

        output = adapters[-1]
        # Num way[i] is the number pf ways to get to i
        num_ways = [0] * (output + 1)
        num_ways[0] = 1

        if 1 in adapters:
            num_ways[1] = 1
        if 2 in adapters and 1 in adapters:
            num_ways[2] = 2
        elif 2 in adapters:
            num_ways[2] = 1

        for n in range(3, output + 1):
            if n not in adapters:
                continue
            num_ways[n] = num_ways[n - 3] + num_ways[n - 2] + num_ways[n - 1]

        return num_ways[output]


#
# ** Testing **
#
TESTCASE = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

# Initialize the Adapter class: adapter
adapter = Adapter(TESTCASE)
assert type(adapter.parse()) == list
assert adapter.count_paths() == 19208

##
# ** Submission process **
##

with open("/Volumes/LocalDiskB/Py/my_advent2020/inputs/day10_input.txt") as f:
    # Initialize the Adapter class: submission_adapter
    submission_adapter = Adapter(f.read())
    print(submission_adapter.multipier())
    print(submission_adapter.count_paths())

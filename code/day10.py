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
    
    def parse(self) -> List[str]:
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


##
### Testing 
##
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


##
### Submission process
##

with open("/Volumes/LocalDiskB/Py/my_advent2020/inputs/day10_input.txt") as f:
    # Initialize the Adapter class: subm_adapter
    subm_adapter = Adapter(f.read())
    print(subm_adapter.multipier())
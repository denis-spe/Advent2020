from typing import Iterator, List

class EncodingError:
    def __init__(self, raw: str) -> None:
        self.raw = raw
        self.valid = []
        self.not_valid = []

    def parse(self) -> List[int]:
        return [int(num) for num in self.raw.split("\n")]

    # Function Copy from Joe Grus
    def not_sum(self, lookback: int = 25) -> Iterator: 
        q = []
        for n in self.parse():
            if len(q) < lookback:
                q.append(n)
            else:
                sum = {
                    a + b
                    for i, a in enumerate(q)
                    for j, b in enumerate(q)
                    if i < j
                }
                if n not in sum:
                    yield n
                
                q.append(n)
                q = q[1:]


#
# UNIT TESTS
#

"""
https://adventofcode.com/2020/day/9
"""
RAW = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

encoder = EncodingError(RAW)

assert next(encoder.not_sum(lookback=5)) == 127

#
# Problem
#
with open("../inputs/day09.txt") as f:
    error_encoder = EncodingError(f.read())
    print(next(error_encoder.not_sum()))


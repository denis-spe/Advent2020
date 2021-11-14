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
    
    def xmas_encrypted_list(self, lookback: int = 25) -> List[int]:
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
                    print(n)
                
                q.append(n)
                q = q[1:]

    def range_with_sum(self, target: int) -> List[int]:
        for i, n in enumerate(self.parse()):
            j = i
            total = n
            while total < target:
                j += 1
                total += self.parse()[j]
            if total == target:
                slice = self.parse()[i: j+1]
                assert sum(slice) == target
                return slice
        raise RuntimeError()

    def encryption_weakness(self, lookback: int = 25) -> int:
        target = next(self.not_sum(lookback))
        slice = self.range_with_sum(target)
        return min(slice) + max(slice)

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
assert encoder.encryption_weakness(5) == 62

#
# Problem
#
with open("../inputs/day09.txt") as f:
    error_encoder = EncodingError(f.read())
    print(next(error_encoder.not_sum()))
    print(error_encoder.encryption_weakness())


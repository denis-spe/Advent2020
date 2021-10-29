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

from typing import List, NamedTuple, Sequence

class Xmas(NamedTuple):
    valid: List[int]
    invalid: List[int]



class EncodingError:
    def __init__(self, raw: str) -> None:
        self.raw = raw
        self.exist = []

    def __parse(self) -> List[int]:
        return [int(num) for num in self.raw.split("\n")]

    def preambling(self, length: int = 5):
        """
        The Function will divde list in nested list
        :Params: length
        :Return: List
        """
        series_of_num = self.__parse()

        previous_num = list(series_of_num[:length])
        print(previous_num)
        


            


        

encoder = EncodingError(RAW).preambling()
print(encoder)



"""
https://adventofcode.com/2020/day/6
"""
import re
from collections import Counter
from typing import List, NamedTuple, Dict

class Answers(NamedTuple):
    yes: int
    no: int 

def answered(question: str) -> int:
    questions = ['a', 'b', 'c', 'x', 'y', 'z']
    if question in questions:
        return 1
    return 0
   


def group(groups: str) -> List[str]:
    return re.split(r'(?:\r?\n){2,}', groups.strip())

def people(groups: group) -> List[List[str]]:
    return [group.split('\n') for group in group(groups=groups)]


def each_person(groups: group) -> int:
    total_people: int = 0
    for person in people(groups):
        # human = ([answered(p) for p in set(person) if len(p) == 1 ])
        total_people += len([answered(val) for val in set(''.join(person))])
    return total_people



def count_yeses(sample: str) -> int:
    groups = sample.strip().split('\n\n')
    num_yeses = 0
    for group in groups:
        people = group.split('\n')
        yeses = Counter(c for person in people for c in person)
        num_yeses += sum(count == len(people) for c, count in yeses.items())
    return num_yeses



 




SAMPLE = """abc

a
b
c

ab
ac

a
a
a
a

b
"""

if __name__ == '__main__':
    assert each_person(SAMPLE) == 11
    assert count_yeses(SAMPLE) == 6
    with open('./inputs/day06_2.txt', 'r') as file:
        print(count_yeses(file.read()))


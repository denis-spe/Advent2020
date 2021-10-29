import re
from typing import Dict, List, NamedTuple, Tuple
from collections import defaultdict

"""
https://adventofcode.com/2020/day/7
"""
RAW1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

RAW2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


class Bags(NamedTuple):
    colored: str
    contains: Dict[str, str]


def bags_container(raws: str) -> List[Bags]:
    color_codeds: List[Bags] = []
    for raw in raws.split('\n'):
        bag, color_coled_bags = raw.strip('.').split(" contain ")
            
        color_coled_bags = re.sub(r'\sbags|\sbag', '', color_coled_bags).strip()
        bag = re.sub('\sbags$|\sbag$', '', bag)
        if 'no other' in color_coled_bags:
            color_codeds.append(Bags(bag, {}))
        else:
            coded = [[val for val in color_bag.strip().split(' ', maxsplit=1)] for color_bag in color_coled_bags.split(',') ]
            color_codeds.append(Bags(bag, {color_bag.strip(): count for count, color_bag in coded}))
                    
    return color_codeds


def parents(bags: List[Bags]) -> Dict[str, List[str]]:
    ic = defaultdict(list)
    for bag in bags:
        for child in bag.contains:
            ic[child].append(bag.colored)
    return ic


def can_eventually_contain(bags: List[Bags], color: str) -> List[str]:
    container = bags_container(bags)
    parent_map = parents(container)
    check_me = [color]
    can_contain = set()
    while check_me:
        child = check_me.pop()
        for parent in parent_map.get(child, []):
            if parent not in can_contain:
                can_contain.add(parent)
                check_me.append(parent)
    return len(list(can_contain))


def num_bag_inside(bags: List[Bags], color: str) -> int:
    by_color = {bag.colored: bag for bag in bags}
    
    num_bags = 0
    stack: List[Tuple[str, int]] = [(color, 1)]
    while stack:
        next_color, multiplier = stack.pop()
        bag = by_color[next_color]
        for child, count in bag.contains.items():
            num_bags += int(multiplier) * int(count)
            stack.append((child, int(count) * int(multiplier)))
    return num_bags

BAGS1 = bags_container(RAW1)
BAGS2 = bags_container(RAW2)


if __name__ == '__main__':
    with open('./inputs/day07_input.txt', mode='r') as file:
        raw = file.read().strip()
        bags = bags_container(raw)
        print(num_bag_inside(bags, 'shiny gold'))
        #print(can_eventually_contain(file.read().strip(), 'shiny gold'))
        #print(parents(bags_container(RAW)))



        





        
    

    

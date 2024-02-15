from __future__ import annotations
from typing import List


def earliest_bus(depart: int, buses: List[int]) -> int:
    missed_by = [depart % bus for bus in buses]
    waits = {
        bus: bus - miss if miss > 0 else 0
        for bus, miss in zip(buses, missed_by)
    }

    # Choose the bus with the lowest wait
    bus = min(buses, key=lambda bus: waits[bus])

    return bus * waits[bus]


#
# Unit tests
#
RAW = """939
7,13,x,x,59,x,31,19"""

L1, L2 = RAW.split("\n")
DEPART = int(L1)
BUSES = [
    int(x) for x in L2.split(',')
    if x != 'x'
]

assert earliest_bus(DEPART, BUSES) == 295

#
# Problem
#
with open("/Volumes/Shortage/Py/Advents/Advent2020/inputs/day13.txt") as f:
    depart = int(next(f))
    buses = [
        int(x) for x in next(f).split(',')
        if x != 'x'
    ]
    print(earliest_bus(depart, buses))


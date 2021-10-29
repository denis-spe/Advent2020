import re
from typing import Dict, List, Tuple

"""
https://adventofcode.com/2020/day/8
"""


def boot_code(raw: str) -> List[Dict[str, str]]:
    # Strip first and last space in the string and then
    # split by newline
    lines = [re.split(r'\s', line)
             for line in raw.strip().split('\n')
             ]
    instructions = [
        {op: arg}
        for op, arg in lines
    ]
    return instructions


class Program:
    def __init__(self, raw: str) -> None:
        self.boot: List[Dict[str, str]] = boot_code(raw)
        self.acc = 0
        self.jmp = 0
        self.nop = 0

    def core_processor(self) -> List[Tuple[str, str]]:
        instructions: List[int] = []
        for inst in self.boot:
            for key, value in inst.items():
                instructions.append((key, value))

        index = 0
        jmp_values = []
        while index < len(instructions):
            if 'nop' in instructions[index]:
                pass
            if 'acc' in instructions[index]:
                pass
            if 'jmp' in instructions[index]:
                index += int(instructions[index][1])
                continue
            
            if index in jmp_values:
                break
            jmp_values.append(index)
            index += 1

        return [
            instructions[jmp]
            for jmp in jmp_values
        ]
        

    def run(self) -> int:
        """
        Return accumulator values
        """
        # Call the Core object
        core = self.core_processor()

        acc = 0
        # loop through the core values
        for tup in core:
            if "acc" in tup:
                acc += int(tup[1])
        return acc

    

TESTCASE = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

def fixing_boot_code(raw: str) -> boot_code:
    """
    Fixing the boot code for proper termination
    """
    # Get the boot code 
    boot = boot_code(raw)

    acc = 0

    executed = set()
    for code in boot:
        for key, value in code.items():
            if key == "Jmp":
                idx=key
                while idx not in executed:
                    executed.add(idx)
                    return True
                return False

            elif key == "nop":
                continue

            else:
                acc += int(value)
    return acc

        





def fixing_program(raw: str) -> int:
    """
    Configing the Program class by changing 
    the boot_code to fixing boot code
    """
    # Call the Program object
    # program = Program(raw)
    # program.boot = fixing_boot_code(raw)
    # return program.run()
    return fixing_boot_code(raw)


RAW = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

if __name__ == '__main__':
    with open('/Volumes/GoogleDrive/My Drive/my_advent2020/inputs/day08_part2.txt', 'r') as file:
        print(fixing_program(RAW))

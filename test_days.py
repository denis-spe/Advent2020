import unittest
from code.day08 import Program, fixing_program

class TestCases(unittest.TestCase):
    def test_day08(self):
        RAW = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
            """
        self.assertEqual(Program(RAW).run(), 5, "Faild")
        self.assertEqual(fixing_program(RAW), 8, "Faild")

if __name__ == "__main__":
    unittest.main()
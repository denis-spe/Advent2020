"""
1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 
1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. 
Find the two entries that sum to 2020; 
what do you get if you multiply them together?
"""


def expense_report(phrases: str) -> int:
    # splite phrase in list by newline
    phrases_list = phrases.strip().split("\n")

    # Variable for storing phrases as int value
    int_phrases = []

    # loop through the phrases list
    for phrase in phrases_list:
        int_phrases.append(int(phrase))

    # initailizing variables
    first_num = 0
    second_num = 1

    # int_phrases length
    length = len(int_phrases)

    while first_num < length:
        #print(first_num, second_num)
        if int_phrases[first_num] + int_phrases[second_num] != 2020:
            second_num += 1
        if second_num == length:
            second_num = 0
            first_num += 1
        if int_phrases[first_num] + int_phrases[second_num] == 2020:
            print(int_phrases[first_num], int_phrases[second_num])
            print(int_phrases[first_num] * int_phrases[second_num])
            break


SIMPLE = """299
1721
979
366
2991
675
1456"""

# print(expense_report(f.read()))

#assert expense_report(SIMPLE) == 2020

# if __name__ == "__main__":
#     with open("day01_2020.txt", "r") as f:
#         expense_report(f.read())


# Part Two
def another_report(phrases: str) -> int:
    # splite phrase in list by newline
    phrases_list = phrases.strip().split("\n")

    # Variable for storing phrases as int value
    int_phrases = []

    # loop through the phrases list
    for phrase in phrases_list:
        int_phrases.append(int(phrase))

    for first in int_phrases:
        for second in int_phrases:
            for third in int_phrases:
                if (first + second + third) == 2020:
                    return (first, second, third), (first + second + third), (first * second * third)
                    break


part_two = """200
1721
9791
3661
2991
99
6751
1456"""


if __name__ == "__main__":
    with open("day01_2020.txt", "r") as f:
        print(another_report(f.read()))

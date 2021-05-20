"""
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

from typing import NamedTuple, List


class ValidPasswords(NamedTuple):
    valid: int
    not_valid: int


class PasswordPhilosophy:
    def __init__(self, password_str: str) -> None:
        self.password_str = password_str

    def __string_process(self):
        """
        The private functions return list of string
        """

        cleaned_lists = []
        str_on_each_line = self.password_str.split('\n')

        for string in str_on_each_line:
            clean_str = string.replace('-', ' ')
            clean_semicoln = clean_str.replace(':', "")
            clean_str = clean_semicoln.split()
            cleaned_lists.append(clean_str)

        return cleaned_lists

    def valider(self):
        valid_password = 0
        invalid_password = 0
        for str_list in self.__string_process():
            if str_list != []:
                value_count = str_list[3].count(str_list[2])
                min_num = int(str_list[0])
                max_num = int(str_list[1])
                if value_count >= min_num and value_count <= max_num:
                    valid_password += 1
                else:
                    invalid_password += 1

        return ValidPasswords(valid=valid_password, 
                                not_valid=invalid_password)

# simple of testcase
passwords = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

# passwords_valider = PasswordPhilosophy(passwords)

# if __name__ == "__main__":
#     print(passwords_valider.valider())

#     with open('day2_input.txt', mode='r') as f:
#         testcase_valider = PasswordPhilosophy(f.read())
#         print(testcase_valider.valider())



# part 2


class PasswordLetters:
    def __init__(self, password_str: str) -> None:
        self.password_str = password_str

    def __string_process(self) -> List[str]:
        """
        The private functions return list of string
        """

        cleaned_lists = []
        str_on_each_line = self.password_str.split('\n')

        for string in str_on_each_line:
            clean_str = string.replace('-', ' ')
            clean_semicoln = clean_str.replace(':', "")
            clean_str = clean_semicoln.split()
            cleaned_lists.append(clean_str)

        return cleaned_lists

    def valider(self) -> ValidPasswords:
        valid_password = 0
        invalid_password = 0
        counter = 0
        for str_list in self.__string_process():
            if str_list != []:
                # Assign values from the list
                phrase: str = str_list[3]
                match_char: str = str_list[2]
                first_num: int = int(str_list[0])
                second_num: int = int(str_list[1])
                set_phrase = set(list(phrase))
                # if second_num index is not match_char and first_num is match_char or 
                # first_num index is not match_char and second_num is match_char
                if (phrase[second_num - 1] == match_char and phrase[first_num - 1] != match_char)\
                     or (phrase[first_num - 1] == match_char and phrase[second_num - 1] != match_char):
                    valid_password += 1
                    
                else:
                    invalid_password += 1

        return ValidPasswords(valid=valid_password, not_valid=invalid_password)


passwords = """2-3 a: bacdel
1-3 b: cdefg
2-9 c: ccccccccc"""

passwords_valider_by_letter = PasswordLetters(passwords)

if __name__ == "__main__":
    print(passwords_valider_by_letter.valider())

    with open('day2_input2.text', mode='r') as f:
        testcase_valider = PasswordLetters(f.read())
        print(testcase_valider.valider())
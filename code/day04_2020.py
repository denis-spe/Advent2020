"""
--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, 
nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
"""
import re
from typing import Dict, NamedTuple, List
import doctest


class ValidPassport(NamedTuple):
    valid: Dict[str, str]
    invalid: Dict[str, str]


class System:
    def __init__(self) -> None:
        self.valid_passport = ValidPassport

    @staticmethod
    def passport_data(data: str) -> Dict[str, str]:
        """
        The function takes string of characters seperated by blank lines
        and :return: dictionary of key and values
        >>> System.passport_data('ecl:gry pid:860033327')
        {0: ['ecl:gry', 'pid:860033327']}
        """

        # list of strings
        passports: List[str] = []

        # processing passport dictionary
        passport_dict: Dict[int, List[str]] = {}

        # Split texts in data by blank line
        blank_line_regex = r"(?:\r?\n){2,}"
        each_passport = re.split(blank_line_regex, data.strip())

        for passport_num, each_pass in enumerate(each_passport):
            passport_dict[passport_num] = re.split(r"\n|[' ']", each_pass)

        return passport_dict


def each_person_passport(passports: str) -> List[Dict[str, str]]:
    """
    This takes the dictionay of keys and values and 
    :return: adictionary of int and dictionary
    >>> each_person_passport('ecl:gry pid:860033327')
    [{'ecl': 'gry', 'pid': '860033327'}]
    """
    # Initialize the System class
    system = System.passport_data(passports)

    each_passport: List[Dict[str, str]] = []
    for key, value in system.items():
        var = [[v for v in val.split(':')] for val in value]
        each_passport.append({KEY: VAL for KEY, VAL in var})

    return each_passport


def passport_validitor(passports: str) -> int:
    """
    Passport_validitor take string and check if passports are valid
    """
    requirements = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        'cid'
    ]
    # Function for string process
    list_of_passports = each_person_passport(passports)

    num_of_valid_passpord = 0
    for passport in list_of_passports:
        if 'byr' in passport.keys() and\
            'iyr' in passport.keys() and 'eyr' in passport.keys() and\
            'hgt' in passport.keys() and 'hcl' in passport.keys() and\
                'ecl' in passport.keys() and 'pid' in passport.keys():
            if 'cid' in passport.keys() or 'cid' not in passport.keys():
                # print(passport)
                num_of_valid_passpord += 1

        else:
            num_of_valid_passpord += 0

    return num_of_valid_passpord


def years(full_passports: Dict[str, str], key: str, start: int, end: int) -> bool:
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    """

    if full_passports[key].isdigit() and len(full_passports[key]) == 4\
            and int(full_passports[key]) >= start and int(full_passports[key]) <= end:
        return True

    return False


def height(full_passports: Dict[str, str], key: str = "hgt") -> bool:
    """
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    if full_passports[key].endswith('cm') or full_passports[key].endswith('in'):
        # taking only the digits from full_passports[key]
        digits = "".join(re.findall(r'\d+', full_passports[key]))
        num = int(digits)
        if 'cm' in full_passports[key]:
            # Check if the number is greater then 150 or less than 193
            if num >= 150 and num <= 193:
                return True
            else:
                return False

        elif 'in' in full_passports[key]:
            # Check if the number is greater then 150 or less than 193
            if num >= 59 and num <= 76:
                return True
            else:
                return False
    else:
        return False


def hair_color(full_passports: Dict[str, str], key: str = "hcl") -> bool:
    """
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    if full_passports[key].startswith('#') and len(full_passports[key][1:]) == 6:
        match = re.findall(r'[0-9]+|[a-f]+', full_passports[key])
        if len('#' + "".join(match)) == len(full_passports[key]):
            return True
        return False
    return False


def eye_color(full_passports: Dict[str, str], key: str = "ecl") -> bool:
    """
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    # ecl must have either of these in the list
    field = re.split(r'\s', 'amb blu brn gry grn hzl oth')

    if full_passports[key] in field:
        return True
    return False


def passport_id(full_passports: Dict[str, str], key: str = "pid") -> bool:
    """
        pid (Passport ID) - a nine-digit number, including leading zeroes.
    """
    if len(full_passports[key]) == 9:
        return True
    return False


def country_id(full_passports: Dict[str, str], key: str = 'cid') -> bool:
    """
        cid (Country ID) - ignored, missing or not.
    """
    if len(full_passports[key]) <= 3:
        return True
    return False


def passport_field(passports: str) -> int:
    """
    Passport_field take string and check if passports are valid according to the fields of passport
    A valid passport must have the following:
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    requirements = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        'cid'
    ]
    # Function for string process
    list_of_passports = each_person_passport(passports)
    num_of_valid_passpord = 0
    for passport in list_of_passports:
        keys = passport.keys()
        if 'byr' in keys and\
            'iyr' in keys and 'eyr' in keys and\
            'hgt' in keys and 'hcl' in keys and\
                'ecl' in keys and 'pid' in keys:
            if 'cid' in keys or 'cid' not in keys:
                if years(full_passports=passport, key='byr', start=1920, end=2002):
                    if years(full_passports=passport, key='iyr', start=2010, end=2020):
                        if years(full_passports=passport, key='eyr', start=2020, end=2030):
                            if height(full_passports=passport):
                                if hair_color(full_passports=passport):
                                    if eye_color(full_passports=passport):
                                        if passport_id(full_passports=passport):
                                            #print(passport)
                                            num_of_valid_passpord += 1

        else:
            num_of_valid_passpord += 0

    return num_of_valid_passpord


SAMPLECASES = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in """

SECONDTESTCASE = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

if __name__ == '__main__':
    doctest.testmod()
    #print(passport_field(SECONDTESTCASE))
    assert passport_validitor(SAMPLECASES) == 2
    assert passport_field(SECONDTESTCASE) == 4
    with open('./inputs/day04_input2.txt', 'r') as file:
        print(passport_field(file.read()))

from typing import List
import dataclasses as dc

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def is_valid(keys: List[str]) -> bool:
    # cid is not required
    intersection_keys = set(keys).intersection(set(required_keys))
    if intersection_keys == set(required_keys):
        return True
    return False

def parse_keys(lines:List[List[str]]) -> List[str]:
    keys = []
    splitted_line = lines.split()
    for l in splitted_line:
        k, _ = l.split(':')
        keys.append(k)
    return keys

with open("day4_passport_processing/example_input.txt") as f:
    lines = f.read()

passport_data = lines.split('\n\n')
for passport in passport_data:
    print(is_valid(parse_keys(passport)))



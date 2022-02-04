from typing import List, Dict
import dataclasses as dc
import re

@dc.dataclass
class Passport:
    byr: str
    iyr: str
    eyr: str
    hgt: float
    hcl: str
    ecl: str
    pid: str

    def validate_correctness(self) -> bool:
        if not (1920 <= int(self.byr) <= 2002) | (len(self.byr) != 4):
            return False
        if not (2010 <= int(self.iyr) <= 2020) | (len(self.iyr) != 4):
            return False
        if not (2020 <= int(self.eyr) <= 2030) | (len(self.eyr) != 4):
            return False
        if "in" in self.hgt:
            if not (59 <= int(self.hgt[:-2]) <= 76):
                return False
        if "cm" in self.hgt:
            if not (150 <= int(self.hgt[:-2]) <= 193):
                return False
        month_day_regex = re.compile(
            r"^#[a-z0-9]{6}"
        )
        match = month_day_regex.match(self.hcl)
        if not match:
            return False
        if self.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        if len(self.pid) != 9:
            return False
        return True


required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def is_valid(passport_dict: dict) -> bool:
    intersection_keys = set(passport_dict.keys()).intersection(set(required_keys))
    if intersection_keys == set(required_keys):
        passport = Passport(
            byr=passport_dict["byr"],
            iyr=passport_dict["iyr"],
            eyr=passport_dict["eyr"],
            hgt=passport_dict["hgt"],
            hcl=passport_dict["hcl"],
            ecl=passport_dict["ecl"],
            pid=passport_dict["pid"],
        )
        return passport.validate_correctness()
    return False


def parse_keys(lines: List[List[str]]) -> dict:
    passport = {}
    splitted_line = lines.split()
    for l in splitted_line:
        k, v = l.split(":")
        passport[k] = v
    return passport


with open("day4_passport_processing/input.txt") as f:
    lines = f.read()

passport_data = lines.split("\n\n")

res = [is_valid(parse_keys(passport)) for passport in passport_data]
print(sum(res))

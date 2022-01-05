import re
import dataclasses as dc

with open("day2_password_philosophy/input.txt") as f:
    lines = f.read().splitlines()

# part one

@dc.dataclass
class PasswordRules:
    letter: str
    min_occurence: int
    max_occurence: int


def parse_line(line: str):
    rules, pw = line.split(":")
    month_day_regex = re.compile(
        r"^(?P<min>\d{1,2})-(?P<max>\d{1,2}) (?P<letter>[a-z])$"
    )
    match = month_day_regex.match(rules)
    pw_rules = PasswordRules(
        letter=match.group("letter"),
        min_occurence=int(match.group("min")),
        max_occurence=int(match.group("max")),
    )

    return pw, pw_rules


def check_validness_pw(password: str, pw_rules: PasswordRules) -> int:
    count = password.count(pw_rules.letter)
    if pw_rules.min_occurence <= count <= pw_rules.max_occurence:
        return 1
    return 0


valid_count = 0
for line in lines:
    pw, rule = parse_line(line)
    valid_count += check_validness_pw(pw, rule)

print(valid_count)

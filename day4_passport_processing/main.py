from typing import List
with open("day4_passport_processing/example_input.txt") as f:
    lines = f.read().splitlines()

def parse_keys(lines:List[List[str]]) -> List[dict]:
    keys = []
    for line in lines:
        splitted_line = line.split()
        for l in splitted_line:
            k, _ = l.split(':')
            keys.append(k)


print(lines)
from itertools import combinations

with open("day1_report_repair/input.txt") as f:
    lines = f.read().splitlines()

lines = [int(line) for line in lines]

# part one
for entries in list(combinations(lines, 2)):
    n1, n2 = entries[0], entries[1]
    if n1 + n2 == 2020:
        print(n1, n2)
        print(n1 * n2)
        break

# part two
for entries in list(combinations(lines, 3)):
    n1, n2, n3 = entries[0], entries[1], entries[2]
    if n1 + n2 + n3 == 2020:
        print(n1, n2, n3)
        print(n1 * n2 * n3)
        break

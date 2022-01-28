from typing import List

with open("day3_toboggan_trajectory/input.txt") as f:
    lines = f.read().splitlines()

def part_one(map: List[List[str]], h_move: int, v_move: int) -> int:
    x = 0
    y = 0
    trees_encountered = 0
    while y != len(map): # if your position is at the last row of the map, stop
        x = x % len(map[0]) # instead of 'copying' the map to the right, I use modulo to traverse the same map instead
        if map[y][x] == '#':
            trees_encountered += 1
        
        x += h_move
        y += v_move

    return trees_encountered

print(part_one(lines, 3, 1))
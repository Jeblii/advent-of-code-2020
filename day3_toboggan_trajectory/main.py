from typing import List
import numpy as np

with open("day3_toboggan_trajectory/input.txt") as f:
    lines = f.read().splitlines()


def traverse_map(map: List[List[str]], h_move: int, v_move: int) -> int:
    x = 0
    y = 0
    trees_encountered = 0
    while True:  # if your position is at the last row of the map, stop
        x = x % len(
            map[0]
        )  # instead of 'copying' the map to the right, I use modulo to traverse the same map instead
        if map[y][x] == "#":
            trees_encountered += 1

        x += h_move
        y += v_move

        if y >= len(map):
            break

    return trees_encountered


# print(part_one(lines, 3, 1))

# part two
options = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
answers = [traverse_map(lines, option[0], option[1]) for option in options]
result = np.prod(np.array(answers))

print(result)

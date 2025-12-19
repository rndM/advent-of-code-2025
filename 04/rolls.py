#!/usr/bin/env python3

def find_accessible_rolls(grid):

    nb_lines = len(grid)
    nb_rows = len(grid[0])
    accessible = []

    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # upper-left, up, upper-right
        (0, -1),          (0, 1),    # left, right
        (1, -1), (1, 0), (1, 1)      # lower-left, down, lower-right
    ]

    for line in range(nb_lines):
        for row in range(nb_rows):
            current = grid[line][row]
            if current != '@':
                continue

            rolls_around = 0

            for delta in directions:
                next_l = line + delta[0]
                next_r = row + delta[1]

                if (0 <= next_l < nb_lines and 0 <= next_r < nb_rows):
                    if grid[next_l][next_r] == '@':
                        rolls_around += 1

            if rolls_around < 4:
                accessible.append((line, row))

    return accessible


def part1(grid):

    accessible = find_accessible_rolls(grid)
    return len(accessible)


def part2(grid):

    grid_copy = [row[:] for row in grid]

    total_removed = 0
    iteration = 0

    while True:
        accessible = find_accessible_rolls(grid_copy)

        if len(accessible) == 0:
            break

        iteration += 1
        print(f"iteration {iteration}: {len(accessible)} rolls to remove")

        for line, row in accessible:
            grid_copy[line][row] = '.'

        total_removed += len(accessible)

    return total_removed


def main():
    with open("input.txt", "r") as file:
        lines = [line for line in file]

    grid = [list(line) for line in lines]

    result_part1 = part1(grid)
    print(f"Part 1 - accessible rolls : {result_part1}")

    result_part2 = part2(grid)
    print(f"Part 2 - removed rolls : {result_part2}")


if __name__ == "__main__":
    main()

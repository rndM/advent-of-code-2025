#!/usr/bin/env python3

def rolls_counter(grid):
    """
    Compte les rouleaux '@' accessibles par un chariot élévateur.
    Un rouleau est accessible s'il a moins de 4 autres rouleaux dans les 8
    cases qui l'entourent.
    """
    nb_lines = len(grid)
    nb_rows = len(grid[0])
    total = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # haut-gauche, haut, haut-droit
        (0, -1),           (0, 1),   # gauche, droite
        (1, -1),  (1, 0),  (1, 1)    # bas-gauche, bas, bas-droit
    ]

    for line in range(nb_lines):
        for rows in range(nb_rows):

            current = grid[line][rows]
            if current != '@':
                continue

            rolls_arround = 0

            for delta_l, delta_r in directions:
                next_l = line + delta_l
                next_r = rows + delta_r

                if (0 <= next_l < nb_lines and 0 <= next_r < nb_rows):
                    if grid[next_l][next_r] == '@':
                        rolls_arround += 1

            if rolls_arround < 4:
                total += 1

    return total


def main():

    with open("input.txt", "r") as file:
        lines = [line for line in file]

    grid = [list(line) for line in lines]

    resultat = rolls_counter(grid)

    print(f"Rouleaux accessibles : {resultat}")


if __name__ == "__main__":
    main()

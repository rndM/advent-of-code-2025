#!/usr/bin/env python3

def parse_input(filename):
    """ Parse le fichier et extrait les intervalles et les IDs """

    with open(filename, 'r') as f:
        content = f.read().strip()

    # Separer les ranges des IDs
    ranges_text, ids_text = content.split('\n\n')

    # stocker tout les ranges dans une liste de tuples
    fresh_ranges = []
    for line in ranges_text.strip().split('\n'):
        start, end = map(int, line.split('-'))
        fresh_ranges.append((start, end))

    # stocker tout les Ids dans une liste de int
    available_ids = []
    for line in ids_text.strip().split('\n'):
        available_ids.append(int(line))

    return fresh_ranges, available_ids


def solve_part1(fresh_ranges, available_ids):
    """ Algo : force brute """

    # pour chaque ID, on vérifie s'il appartient à au moins un range
    # Complexité : O(IDs x ranges)
    fresh_count = 0

    for ingredient_id in available_ids:
        is_fresh = False
        for start, end in fresh_ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1

    return fresh_count


def solve_part2(fresh_ranges):
    """ Algo : interval merging.
    fusionner les intervalles chevauchants et adjacents
    Complexité : O(n log n) """

    # Trier les ranges par début croissant
    sorted_ranges = sorted(fresh_ranges)

    merged = list()

    curr_start, curr_end = sorted_ranges[0]

    for next_start, next_end in sorted_ranges[1:]:
        # fusionner si le prochain intervalle chevauche ou touche le courant
        if next_start <= curr_end + 1:
            curr_end = max(curr_end, next_end)
        else:
            # sinon, ajouter l'intervalle courant et en démarrer un autre
            merged.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end

    # ajouter le dernier intervalle
    merged.append((curr_start, curr_end))

    # total
    return sum((end - start + 1) for start, end in merged)


def main():
    filename = 'input.txt'
    fresh_ranges, available_ids = parse_input(filename)

    print("Part 1 :", solve_part1(fresh_ranges, available_ids))
    print("Part 2 :", solve_part2(fresh_ranges))


if __name__ == "__main__":
    main()

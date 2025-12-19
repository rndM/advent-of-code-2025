#!/usr/bin/env python3

def count_fresh_ingredients(filename):

    with open(filename, 'r') as f:
        content = f.read().strip()

    # Separer les ranges des IDs
    parts = content.split('\n\n')
    ranges_text = parts[0]
    ids_text = parts[1]

    # stocker les ranges dans une liste de tuples
    fresh_ranges = []
    for line in ranges_text.strip().split('\n'):
        start, end = map(int, line.split('-'))
        fresh_ranges.append((start, end))

    # stocker les Ids dans une liste de int
    available_ids = []
    for line in ids_text.strip().split('\n'):
        available_ids.append(int(line))

    # Est-ce que chaque ID tombe dans au moins un des intervalles ?
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


def main():
    filename = 'input.txt'

    result = count_fresh_ingredients(filename)
    print("Part 1 :", result)


if __name__ == "__main__":
    main()

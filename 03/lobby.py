#!/usr/bin/env python3

def max_joltage_k_batteries(line, k):
    """
    Trouve le voltage maximum en sélectionnant exactement k batteries.
    Choisir le plus grand chiffre disponible qui permet encore de
    sélectionner k batteries au total.
    """
    n = len(line)
    if k > n:
        return 0

    result = []
    start = 0

    for pos in range(k):
        # Nombre de batteries restantes à sélectionner après celle-ci
        remaining = k - pos - 1

        # On cherche le plus grand chiffre dans la fenêtre valide
        # On doit laisser au moins 'remaining' batteries après
        max_digit = -1
        max_idx = -1

        for i in range(start, n - remaining):
            digit = int(line[i])
            if digit > max_digit:
                max_digit = digit
                max_idx = i

        result.append(str(max_digit))
        start = max_idx + 1

    return int(''.join(result))


def main():
    total_joltage_part1 = 0
    total_joltage_part2 = 0

    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    for line in lines:
        max_joltage = max_joltage_k_batteries(line, 2)
        total_joltage_part1 += max_joltage

    print(f"Part 1 : {total_joltage_part1}")

    for line in lines:
        max_joltage = max_joltage_k_batteries(line, 12)
        total_joltage_part2 += max_joltage

    print(f"Part 2 : {total_joltage_part2}")


if __name__ == "__main__":
    main()

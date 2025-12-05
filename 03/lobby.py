#!/usr/bin/env python3


# garder les deux plus grand chiffres de chaques ligne et en faire un nombre
# additionner tout les nombres pour trouver le joltage
def main():
    max_joltage = 0

    with open('input.txt', 'r') as f:
        file = f.read().split('\n')

    for line in file:
        joltage = []

        bank = [int(i) for i in line]

        for i in range(2):
            digit = 0
            for battery in bank:
                digit = max(digit, battery)
            joltage.append(digit)
            if digit in bank:
                bank.remove(digit)
            max_joltage += int(joltage)
            print(joltage)

    print(max_joltage)


if __name__ == "__main__":
    main()


""" def main():
    joltage_output = 0

    with open('input.txt', 'r') as f:
        file = f.read().split('\n')

    for line in file:
        max_joltage = 0
        print(line)
        for i in range(len(line) - 1):
            joltage = int(line[i:i+2])
            max_joltage = max(max_joltage, joltage)
        joltage_output += max_joltage

    print(joltage_output) """

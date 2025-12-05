#!/usr/bin/env python3

def main():
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

    print(joltage_output)


if __name__ == "__main__":
    main()

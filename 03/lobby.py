#!/usr/bin/env python3

def main():
    total_joltage = 0

    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')

    for line in lines:
        max_joltage = 0

        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                joltage = int(line[i] + line[j])
                max_joltage = max(max_joltage, joltage)

        total_joltage += max_joltage

    print(f"output joltage: {total_joltage}")


if __name__ == "__main__":
    main()

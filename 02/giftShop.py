#!/usr/bin/env python3

# Un numero est invalide si il contient un pattern repete 2 fois
def is_invalid_part1(num):
    s = str(num)
    length = len(s)

    if length % 2 != 0:
        return False

    mid = length // 2
    first = s[:mid]
    second = s[mid:]

    return first == second


# Un numero est invalide si il contient un pattern repete au moins 2 fois
def is_invalid_part2(num):
    s = str(num)
    length = len(s)

    for digits in range(1, length // 2 + 1):
        if length % digits == 0:
            pattern = s[:digits]
            rep = length // digits
            if rep >= 2 and pattern * rep == s:
                return True
    return False


def solve(part, ids):
    res = 0

    for id in ids:
        start, end = id.split('-')
        start = int(start)
        end = int(end)

        for num in range(start, end + 1):
            if part == 1 and is_invalid_part1(num):
                res += num
            elif part == 2 and is_invalid_part2(num):
                res += num
    return res


def main():

    with open('input.txt', 'r') as f:
        datas = f.read().strip().split(',')

    print(f"Part 1: {solve(1, datas)}")
    print(f"Part 2: {solve(2, datas)}")


if __name__ == "__main__":
    main()

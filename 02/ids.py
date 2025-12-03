#!/usr/bin/env python3

def is_invalid(num):
    s = str(num)
    length = len(s)

    if length % 2 != 0:
        return False

    mid = length // 2
    first = s[:mid]
    second = s[mid:]

    return first == second


def main():

    with open('input.txt', 'r') as f:
        file = f.read()

    ids = file.split(',')

    res = 0

    for id in ids:
        start, end = id.split('-')
        start = int(start)
        end = int(end)

        print("Plage:", start, " à ", end)

        for num in range(start, end + 1):
            if is_invalid(num):
                print(num, "est invalide")
                res += num

    print(f"\nres: {res}")


if __name__ == "__main__":
    main()

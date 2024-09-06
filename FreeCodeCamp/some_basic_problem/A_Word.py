import math


def main():
    str = input()

    up = 0
    lw = 0

    for i in str:
        if i.islower():
            lw += 1
        else:
            up += 1

    if lw >= up:
        print(str.lower())
    else:
        print(str.upper())


if __name__ == "__main__":
    main()

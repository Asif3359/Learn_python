import math


def main():
    n = int(input("Enter Element Number :"))

    value = set()

    for i in range(n):
        a = int(input("Number :"))
        value.add(a)
    print(value)


if __name__ == "__main__":
    main()

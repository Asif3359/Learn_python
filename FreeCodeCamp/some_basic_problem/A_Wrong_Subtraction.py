import math


def main():
    # N = input().split()
    # A = int(N[0])
    # B = int(N[1])

    A, B = map(int, input().split())

    for i in range(B):
        if A % 10 != 0:
            A -= 1
        else:
            A //= 10

    print(A)


if __name__ == "__main__":
    main()

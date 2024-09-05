import math


def fibonacci(n):
    fib_sec = [0, 1]
    for i in range(2, n):
        fib_sec.append(fib_sec[-1] + fib_sec[-2])

    return fib_sec[:n]


def main():
    n = int(input())
    print(fibonacci(n))


if __name__ == "__main__":
    main()

import math


def is_lucky(n):
    """Check if a number is lucky."""
    if n == 0:
        return False
    while n > 0:
        digit = n % 10
        if digit != 7 and digit != 4:
            return False
        n = n // 10

    return True


def count_lucky(n):
    """Count the number of lucky digits in a number."""
    cnt = 0
    while n > 0:
        digit = n % 10
        if digit == 7 or digit == 4:
            cnt += 1
        n = n // 10

    return cnt


def main():
    n = int(input())

    count = count_lucky(n)

    if is_lucky(count):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

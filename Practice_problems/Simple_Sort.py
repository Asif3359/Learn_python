import math


def main():
    nums = list(map(int, input().split()))

    nums1 = []

    for i in nums:
        nums1.append(i)

    nums.sort()

    for i in nums:
        print(i)

    print()

    for i in nums1:
        print(i)


if __name__ == "__main__":
    main()

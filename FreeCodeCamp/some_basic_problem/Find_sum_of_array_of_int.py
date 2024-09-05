def find_sum(arr, n):
    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum


def find_sum(arr):
    return sum(arr)


def main():
    n = int(input())

    arr = []
    for i in range(n):
        a = int(input())
        arr.append(a)

    sum = find_sum(arr)

    print(sum)


if __name__ == "__main__":
    main()

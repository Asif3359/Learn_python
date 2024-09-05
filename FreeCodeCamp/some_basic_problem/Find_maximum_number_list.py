# Example of using finite large integers
max_int = 2**31 - 1  # 2147483647
min_int = -(2**31)  # -2147483648


def find_max(arr, n):
    max = min_int

    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max


def find_max(arr):
    return max(arr)


def find_min(arr, n):
    min = max_int
    for i in range(n):
        if arr[i] < min:
            min = arr[i]
    return min


def find_min(arr):
    return min(arr)


def main():
    n = int(input())
    arr = []
    for i in range(n):
        a = int(input())
        arr.append(a)

    # print(find_max(arr, n))
    # print(find_min(arr, n))
    print(find_max(arr))
    print(find_min(arr))


if __name__ == "__main__":
    main()

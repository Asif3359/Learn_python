import math


def main():
    dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
    dict2 = {"A": -1, "B": -2, "C": -3, "D": -4}

    merge_dict = dict1.copy()
    merge_dict.update(dict2)
    print(merge_dict)


if __name__ == "__main__":
    main()

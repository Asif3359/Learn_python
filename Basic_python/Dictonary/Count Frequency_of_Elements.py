import math


def main():
    elements = ["apple", "banana", "apple", "orange", "banana", "apple"]
    fr_dict = {}
    for element in elements:
        if element in fr_dict:
            fr_dict[element] += 1
        else:
            fr_dict[element] = 1
    print(fr_dict)


if __name__ == "__main__":
    main()

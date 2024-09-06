import math


def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]

    common_elements_dict = {}
    common_elements = set(list1).intersection(list2)

    for element in common_elements:
        common_elements_dict[element] = (list1.count(element), list2.count(element))

    print(common_elements_dict)


if __name__ == "__main__":
    main()

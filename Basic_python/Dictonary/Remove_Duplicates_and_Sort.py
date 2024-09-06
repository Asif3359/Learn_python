import math


def main():
    dict_list = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Alice", "age": 22},
        {"name": "Charlie", "age": 35},
    ]
    # Remove duplicates
    seen = set()
    unique_dict_list = []
    for d in dict_list:
        if d["name"] not in seen:
            unique_dict_list.append(d)
            seen.add(d["name"])

    # Sort by 'name'
    # unique_sorted_dict_list = sorted(unique_dict_list, key=lambda x: x["name"])
    unique_dict_list.sort(key=lambda x: ["name"])
    print(unique_dict_list)


if __name__ == "__main__":
    main()

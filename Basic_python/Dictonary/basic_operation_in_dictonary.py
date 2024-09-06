import math


def main():

    n = int(input())

    user_dic = {}
    for i in range(n):
        key = input("Enter student Name: ")
        value = int(input("Enter Student marks:"))
        user_dic[key] = value

    # total_marks = sum(user_dic.values())
    # print(total_marks)

    # average = total_marks / n
    # print(average)

    # max_marks_student = max(user_dic, key=user_dic.get)
    # max_mark = user_dic[max_marks_student]
    # print(f" {max_marks_student} {max_mark}")

    # sort_dic = dict(sorted(user_dic.items(), key=lambda item: item[1]))
    # print(sort_dic)

    total = 0
    for mark in user_dic.values():
        total += mark
    print(total)

    avg = total / n
    print(avg)

    max_mark_student = None
    max_mark = -float("inf")

    for student, mark in user_dic.items():
        if mark > max_mark:
            max_mark = mark
            max_mark_student = student
    print(f"{student} {max_mark}")

    item_list = list(user_dic.items())
    # print(item_list)

    for i in range(len(item_list)):
        for j in range(0, len(item_list) - i - 1):
            if item_list[j][1] > item_list[j + 1][1]:
                # swap
                item_list[j], item_list[j + 1] = item_list[j + 1], item_list[j]
    sort_dic = dict(item_list)
    print(sort_dic)


if __name__ == "__main__":
    main()

import math


def main():

    n = int(input())

    user_dic = {}
    for i in range(n):
        key = input("Enter student Name: ")
        value = int(input("Enter Student marks:"))
        user_dic[key] = value

    print(user_dic)


if __name__ == "__main__":
    main()

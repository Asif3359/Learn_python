# normal order
def number(num):
    if num == 0:
        return
    number(num - 1)
    print(num)


# reverse order
def number_2(num):
    if num == 0:
        return

    print(num)
    number(num - 1)


print("Normal ")
number(10)
print("Reverse")
number_2(10)

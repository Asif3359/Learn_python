def calculator():
    try:
        num = int(input("Enter a number :"))
        print(num)

        num1 = float(input("Enter first Number :"))
        op = input("Enter Operation :")
        num2 = float(input("Enter second Number :"))

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "/":
            print(num1 / num2)
        elif op == "*":
            print(num1 * num2)
        else:
            print("Envalid operation")
    except ZeroDivisionError:
        print("Deivided by zero")
    except ValueError:
        print("Invalid input")

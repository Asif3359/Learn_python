import math


def main():

    A, B, C = map(float, input().split())

    if A + B > C and A + C > B and B + C > A:

        perimeter = A + B + C
        print(f"Perimetro = {perimeter:.1f}")
    else:

        area = 0.5 * (A + B) * C
        print(f"Area = {area:.1f}")


if __name__ == "__main__":
    main()

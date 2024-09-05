import math


def count_vowels(s):
    vowels = "aeiou"
    s = s.lower()  # Convert string to lowercase
    vowel_count = {vowel: 0 for vowel in vowels}

    for char in s:
        if char in vowels:
            vowel_count[char] += 1

    return vowel_count


def main():
    str = input()
    print(count_vowels(str))


if __name__ == "__main__":
    main()

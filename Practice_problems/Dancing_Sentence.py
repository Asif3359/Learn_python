def make_dancing_sentence(sentence):

    uppercase = True
    result = []

    for char in sentence:
        if char.isalpha():
            if uppercase:
                result.append(char.upper())
            else:
                result.append(char.lower())
            uppercase = not uppercase
        else:
            result.append(char)

    return "".join(result)


def main():
    try:
        while True:

            sentence = input()

            print(make_dancing_sentence(sentence))
    except EOFError:
        pass


if __name__ == "__main__":
    main()

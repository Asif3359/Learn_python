is_male = True
is_tall = True

if is_male and is_tall:
    print("You are male or tall or both")
else:
    print("You nither male nor tall")


if is_male and is_tall:
    print("You are male and tall")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are either not male or not tall or both")

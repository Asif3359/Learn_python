friends = ["Kevin", "Karen", "Jim", "Jim", "Asif", "Toby"]
lucky_numbers = [4, 9, 3, 5, 23, 0]

print(friends)
print(friends[0], friends[1], friends[2])
print(friends[-1], friends[-2], friends[-3])
print(friends[1:])
print(friends[1:3])
friends[4] = "Mike"
print(friends[1:])

friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Mike")
print(friends)
friends.pop()
print(friends)

print(friends.index("Jim"))
print(friends.count("Jim"))

lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)

friends_2 = friends.copy()

print(friends_2)

friends.clear()

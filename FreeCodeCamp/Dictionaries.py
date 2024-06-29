monthConversions = {
    "Jan": "January",
    "Fev": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Mar": "March",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions)
print(monthConversions["Nov"])
print(monthConversions.get("Decc", "Not a valid Key"))

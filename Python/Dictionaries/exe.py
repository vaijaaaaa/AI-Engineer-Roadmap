numbers = {
 "1" : "One",
 "2" : "tow",
 "3" : "three",
 "4" : "four"
}

phone = input("Phone :")

output = ""
for ch in phone:
    output += numbers.get(ch, "!") + " "
print(output)
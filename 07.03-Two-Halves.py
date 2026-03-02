s = input("Enter a string: ")
firsthalf = s[:(len(s)+1) // 2]
secondhalf = s[(len(s)+1) // 2:]
interchanged = secondhalf + firsthalf
print(interchanged)
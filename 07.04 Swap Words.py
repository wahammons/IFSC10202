s = input("Enter a string: ")
firstword = s[:s.find(" ")]
secondword = s[s.find(" ")+1:]
result = secondword + " " + firstword
print(result)
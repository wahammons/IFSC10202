s = input("Enter a string: ")
#find the first h and the last h
firsth = s.find("h")
lasth = s.rfind("h")
#remove the fragment between the first and last h
result = s[:firsth] + s[lasth+1:]
print(result)
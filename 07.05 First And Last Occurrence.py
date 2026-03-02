s = input("Enter a string: ")
if s.count("f") == 1:
    firstf = s.find("f")
    print("{}".format(firstf))
elif s.count("f") > 1:
    firstf = s.find("f")
    lastf = s.rfind("f")
    print("First occurrence of f is at index {}".format(firstf))
    print("Last occurrence of f is at index {}".format(lastf))
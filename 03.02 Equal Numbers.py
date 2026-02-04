a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
if a == b and b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

    

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))
add = num1 + num2 
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
if op == "+":
    print(num1, "+", num2,"=", add)
elif op == "-":
    print(num1, "-", num2,"=", sub)
elif op == "*":
    print(num1, "*", num2,"=", mult)
elif op == "/":
    #move div here and check before if num2 is zero
    
    print(num1, "/", num2,"=", div,)
else:
    print("Invalid Operator")



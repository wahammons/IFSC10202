start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

print(f"Special Numbers between {start} and {end}")

for num in range(start, end + 1):
    a = num
    count = 0
    if a == 0:
        count = 1
    else:
        while a > 0:
            count += 1
            a //= 10
            
    a = num
    total = 0
    while a > 0:
        b = a % 10
        total += (b ** count)
        a //= 10
        
    if total == num and num != 0:
        print(num)
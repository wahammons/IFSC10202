start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

print(f"Special Numbers between {start} and {end}")

for i in range(start, end + 1):
    num = i
    total = 0
    if num == 0:
        total = 1
    else:
        while num > 0:
            total += 1
            num //= 10
num = i
sum = 0      
while num > 0:
        digit = num % 10
        
  
        digit_total = 1
        for _ in range(total):
            digit_total *= digit
            
        sum += digit_total
        num //= 10
        
   
if sum == i and i != 0:
        print(i)
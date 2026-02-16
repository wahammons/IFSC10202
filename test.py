start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

print(f"Special Numbers between {start} and {end}")

for num in range(start, end + 1):
    # Step 1: Count digits
    temp_num = num
    count = 0
    if temp_num == 0:
        count = 1
    else:
        while temp_num > 0:
            count += 1
            temp_num //= 10
            
    # Step 2: Calculate sum of digits raised to the power of 'count'
    temp_num = num
    sum_pow = 0
    while temp_num > 0:
        digit = temp_num % 10
        
        # Calculate digit^count manually or with **
        digit_total = 1
        for _ in range(count):
            digit_total *= digit
            
        sum_pow += digit_total
        temp_num //= 10
        
    # Step 3: Check if it is a special number
    if sum_pow == num and num != 0:
        print(num)
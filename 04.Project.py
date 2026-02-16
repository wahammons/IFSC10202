def print_asterisk(height):
    for i in range(1, height + 1):
        print(*"*" * i)
        
max_height = int(input("Enter maximum height: "))
print_asterisk(max_height)

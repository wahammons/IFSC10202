s="Hello"
print("Hello Forward")
for i in range(0, len(s)):
	print(s[i])
 
print("Hello Backward")
#start at -1, stop at -len(s)-1, step backwards by -1
for i in range(-1, -len(s)-1, -1):
	print(s[i])
# Whitney Hammons

# AI Usage: None

# Number of years in the length of time
# Number of days in the length of time
# Number of hours in the length of time
# Number of minutes in the length of time
# Number of seconds in the length of time

total = int(input("Enter length of time in seconds: "))
m = 60
h = 60* 60
d = 24 * 60 * 60
y = 365 * 24 * 60 * 60

year = total // y
total = total - (y * year)

day = total // d
total = total-(d * day)

hour = total // h
total = total - (h * hour)

minute = total // m
total = total - (m * minute)

sec = total

print(f"Years: {year}")
print(f"Days: {day}")
print(f"Hours: {hour}")
print(f"Minutes: {minute}")
print(f"Seconds: {sec}")
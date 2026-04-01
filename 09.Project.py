file_name = "09.Project Distances.csv"

distance_table = []

with open(file_name, "r") as file:
    for line in file:
        row = line.strip().split(",")
        distance_table.append(row)

for row in distance_table:
    for item in row:
        print(f"{item:>10}", end="")
    print()

from_city = input("Enter From City: ")
to_city = input("Enter To City: ")

from_index = -1
to_index = -1

for i in range(1, len(distance_table)):
    if distance_table[i][0].strip().lower() == from_city.strip().lower():
        from_index = i
        break

for j in range(1, len(distance_table[0])):
    if distance_table[0][j].strip().lower() == to_city.strip().lower():
        to_index = j
        break

if from_index == -1:
    print("Invalid From City")
elif to_index == -1:
    print("Invalid To City")
else:
    distance = distance_table[from_index][to_index]
    print(f"{from_city} to {to_city} - {distance} miles")

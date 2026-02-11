from math import degrees, sin, cos, acos, pi, radians
import math

r = 6371

print("Great Circle Calculator")
r = float(input("Enter Radius of Sphere: "))
lat1 = float(input("Starting Point - Enter Latitude: "))
lon1 = float(input("Starting Point - Enter Longitude: "))
lat2 = float(input("Ending Point - Enter Latitude: "))
lon2 = float(input("Ending Point - Enter Longitude: "))

x1 = math.radians(lat1)
y1 = math.radians(lon1)
x2 = math.radians(lat2)
y2 = math.radians(lon2)

d = r * math.acos((math.sin(x1) * math.sin(x2)) + (math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)))

print(f"The Great Circle Distance is {d:.2f} km") 
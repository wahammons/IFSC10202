from math import pi
#diameter is 2 times the radius
def diameter(r):
    return 2 * r
#circumference is 2 times pi times the radius
def circumference(r):
    return 2 * pi * r
#area is pi times the radius squared
def area(r):
    return pi * r ** 2
print("{:>15} {:>15} {:>15} {:>15}".format("Radius", "Diameter", "Circumference", "Area"))
#Open input file for reading
inputfile = open("06.01 Radius.txt")
#Read the first line
line = inputfile.readline()
#Read until the input is empty
while line != '':
#Convert input line to a floating number
    radius = float(line)
#Print the results
    print("{:15.2f} {:15.2f} {:15.2f} {:15.2f}".format(radius, diameter(radius), circumference(radius), area(radius)))
#Read the next line
    line = inputfile.readline()
#Close file
inputfile.close()
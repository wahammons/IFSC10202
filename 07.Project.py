def ParseDegreeString(ddmmss):
    degree_pos = ddmmss.find(chr(176))   # Degree symbol °
    minute_pos = ddmmss.find("'")        # Minute symbol '
    second_pos = ddmmss.find('"')        # Second symbol "

    degrees = float(ddmmss[:degree_pos])
    minutes = float(ddmmss[degree_pos + 1:minute_pos])
    seconds = float(ddmmss[minute_pos + 1:second_pos])

    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees


def main():
    inputfile = "07.Project Angles Input.txt"
    outputfile = "07.Project Angles Output.txt"
   
    infile = open(inputfile, "r")
    outfile = open(outputfile, "w")
    outputcount = 0
    for line in infile:
        line = line.strip()

        degrees, minutes, seconds = ParseDegreeString(line)
        decimal_value = DDMMSStoDecimal(degrees, minutes, seconds)
        outfile.write(f"{decimal_value:.6f}\n")
        outputcount += 1
    print(f"{outputcount} records processed")
    infile.close()
    outfile.close()
main()

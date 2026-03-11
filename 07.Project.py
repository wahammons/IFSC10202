def ParseDegreeString(ddmmss):
    deg_pos = ddmmss.find(chr(176))   # Degree symbol °
    min_pos = ddmmss.find("'")        # Minute symbol '
    sec_pos = ddmmss.find('"')        # Second symbol "

    degrees = float(ddmmss[:deg_pos])
    minutes = float(ddmmss[deg_pos + 1:min_pos])
    seconds = float(ddmmss[min_pos + 1:sec_pos])

    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees


def main():
    input_file = "07.Project Angles Input.txt"
    output_file = "07.Project Angles Output.txt"

    infile = open(input_file, "r")
    outfile = open(output_file, "w")

    for line in infile:
        line = line.strip()

        degrees, minutes, seconds = ParseDegreeString(line)
        decimal_value = DDMMSStoDecimal(degrees, minutes, seconds)
        outfile.write(f"{line} = {decimal_value:.6f}\n")

    infile.close()
    outfile.close()
main()

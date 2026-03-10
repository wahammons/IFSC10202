def ParseDegreeString(ddmmss):
    # Find symbol positions
    deg_pos = ddmmss.find(chr(176))   # Degree symbol °
    min_pos = ddmmss.find("'")        # Minute symbol '
    sec_pos = ddmmss.find('"')        # Second symbol "

    # Extract values
    degrees = float(ddmmss[:deg_pos])
    minutes = float(ddmmss[deg_pos + 1:min_pos])
    seconds = float(ddmmss[min_pos + 1:sec_pos])

    return degrees, minutes, seconds


# Function to convert DMS to decimal degrees
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

        # Parse the string
        degrees, minutes, seconds = ParseDegreeString(line)

        # Convert to decimal
        decimal_value = DDMMSStoDecimal(degrees, minutes, seconds)

        # Write to output file
        outfile.write(f"{line} = {decimal_value:.6f}\n")

    infile.close()
    outfile.close()
main()

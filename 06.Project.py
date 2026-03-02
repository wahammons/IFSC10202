inputfilename = "06.Project Input File.txt"
outputfilename = "06.Project Output File.txt"
inputfile = open(inputfilename, 'r')
outputfile = open(outputfilename, 'w')
recordcount = 0
line = inputfile.readline()
while line != '':
    outputfile.write(line)
    recordcount += 1
    line = inputfile.readline()
recordcount = 0
inputfile.close()
outputfile.close()
print("{} records written".format(recordcount))
inputfilename = "06.Project Input File.txt"
mergefilename = "06.Project Merge File.txt"
outputfilename = "06.Project Output File.txt"
inputcount = 0
mergecount = 0
outputcount = 0
infile = open(inputfilename, 'r')
outfile = open(outputfilename, 'w')
line = infile.readline()
while line !="":
     if line == '**Insert Merge File Here**\n':
          mergefile = open(mergefilename, 'r')
          mergeLine = mergefile.readline()
          while mergeLine != '':
               outfile.write(mergeLine)
               mergecount += 1
               outputcount += 1
               mergeLine = mergefile.readline()
          mergefile.close()
     else:
          outfile.write(line)
          inputcount += 1
          outputcount += 1

     line = infile.readline()

infile.close()
outfile.close()
print(f"{inputcount} input file records")
print(f"{mergecount} merge file records")
print(f"{outputcount} output file records")

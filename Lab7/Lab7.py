#Lab 7
#reads infile, counts number of alues that meet criteria
#prints as output, writes new outfile

import os.path
endofprogram = False

try:
    readingfile = input("Enter name of input file >")  
    infile = open(readingfile, 'r')
    
    writingfile = input("Enter name of output file >")
    while os.path.isfile(writingfile):
        writingfile = input("File exists. Enter name again >")
    outfile = open(writingfile, 'w')

except IOError:
    print("Error opening file - End of program")
    endofprogram = True

if endofprogram == False:
    count = 0   
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for line in infile:
        line = line.strip()
        if len(line) != 0 and line[0] != '#':
            count = count + 1
        if 'dangerous' in line:
            count1 = count1 + 1
        if 'brown' in line and 'dangerous' in line:
            count2 = count2 + 1
        if 'large' in line and 'safe' in line:
            count3 = count3 + 1
        if 'safe' in line and ('red' in line or 'hard' in line):
            count4 = count4 + 1
        
    print("Total animals =", count)
    outfile.write("Total animals = "+str(count)+'\n')
    
    print("Total dangerous =", count1)
    outfile.write("Total dangerous = "+str(count1)+'\n')
    
    print("Brown and dangerous =", count2)
    outfile.write("Brown and dangerous = "+str(count2)+'\n')
    
    print("Large and safe =", count3)
    outfile.write("Large and safe = "+str(count3)+'\n')
    
    print("Safe and red color or hard flesh =", count4)
    outfile.write("Safe and red color or hard flesh = "+str(count4)+'\n')
    
    infile.close()
    outfile.close()
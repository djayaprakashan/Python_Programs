import os
import re

''' # Another way to open, read and close a file
with open('preproinsulin-seq.txt', 'r') as inFile:
inFile = open('preproinsulin-seq.txt', 'r')
    for data in inFile:
        data = inFile.readlines()
        print(data)    
'''
# Assigning file names to variables
inputFile = "preproinsulin-seq.txt"
outputFile1 = "preproinsulin-seq-clean.txt"
outputFile2 = "Isinsulin-seq-clean.txt"
outputFile3 = "binsulin-seq-clean.txt"
outputFile4 = "cinsulin-seq-clean.txt"
outputFile5 = "ainsulin-seq-clean.txt"


# Opening files to read or write
inFile = open(inputFile, 'r')
outFile1 = open(outputFile1, 'w')
outFile2 = open(outputFile2, "w")
outFile3 = open(outputFile3, "w")
outFile4 = open(outputFile4, "w")
outFile5 = open(outputFile5, "w")
'''
def find_no_of_char(file_name):
    file = open(file_name, 'r')
    file_content = file.read()
    l = len(file_content)
    print(file_name)
    print('***********************************')
    print(file_content)
    print(f"The file {file_name} has " + str(l) + " characters")
    print('***********************************')
'''
seq_full = inFile.read()
#print(seq_full)
#find_no_of_char(inputFile)
#seq_clean = ''


#for char in seq_full:
#    seq_clean += char

for char in seq_full:
    #print(char)
#    if re.match('^[A-Z/0-9]', char):
#        continue
#    else:
        #seq_clean = seq_clean.join(char)
    seq_clean += char
seq_clean = ''.join(filter(str.isalpha, seq_clean))
seq_clean = ''.join(filter(str.islower, seq_clean))

print(f"The file {inputFile} has {len(seq_full)}")

#print(seq_clean)

outFile1.write(seq_clean)
outFile1_data = outFile1.read()
print(f"The file {outputFile1} has {len(outFile1_data)}")




#print(outputFile1)
#find_no_of_char(outputFile1)
#find_no_of_char(outputFile2)

inFile.close()
outFile1.close()

#l = len(seq_clean)
#print("The clean sequence has " + str(l) + " characters")


       
outFile2.close()
outFile3.close()
outFile4.close()
outFile5.close()
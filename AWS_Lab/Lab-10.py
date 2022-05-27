import os
import string
import re

# Reading from the main file and finding number of Charracters in file (preproinsulin-seq.txt) 
inputFile = "preproinsulin-seq.txt"
inFile = open(inputFile, 'r')
seq_full = inFile.read()

seq_clean = ""
for char in seq_full:
    if re.match('^[ A-Z\/0-9/\n/\b/\r]', char):
        continue
    else:
        #seq_clean = seq_clean.join(char)
        seq_clean += char
print(seq_clean)

#seq_clean = ''.join(filter(str.isalpha, seq_full))
#seq_clean = ''.join(filter(str.islower, seq_clean))

print(f"The file {inputFile} has {len(seq_full)} characters")
inFile.close()

# ********************************************************************
# Writing the clean sequence into the file preproinsulin-seq-clean.txt  

outputFile1 = "preproinsulin-seq-clean.txt"
outFile1 = open(outputFile1, 'w')
outFile1.write(seq_clean)
outFile1.close()
outFile1 = open(outputFile1, 'r')
outFile1_data = outFile1.read()
print(f"The file {outputFile1} has {len(outFile1_data)} characters")
outFile1.close()

#*************************************************************************
# Writing only the required sequence into the file Isinsulin-seq-clean.txt

outputFile2 = "Isinsulin-seq-clean.txt"
with open(outputFile2, 'w') as outFile2:
    outFile2.write(seq_clean[0:24])
with open(outputFile2, 'r') as outFile2:
    outFile2_data = outFile2.read()
    print(f"The file {outputFile2} has {len(outFile2_data)} characters")

#**************************************************************************
# Writing only the required sequence into the file binsulin-seq-clean.txt

outputFile3 = "binsulin-seq-clean.txt"
with open(outputFile3, 'w') as outFile3:
    outFile3.write(seq_clean[24:54])
with open(outputFile3, 'r') as outFile3:
    outFile3_data = outFile3.read()
    print(f"The file {outputFile3} has {len(outFile3_data)} characters")

#**************************************************************************
# Writing only the required sequence into the file cinsulin-seq-clean.txt

outputFile4 = "cinsulin-seq-clean.txt"
with open(outputFile4, 'w') as outFile4:
    outFile4.write(seq_clean[54:89])
with open(outputFile4, 'r') as outFile4:
    outFile4_data = outFile4.read()
    print(f"The file {outputFile4} has {len(outFile4_data)} characters")

#**************************************************************************
# Writing only the required sequence into the file ainsulin-seq-clean.txt

outputFile5 = "ainsulin-seq-clean.txt"
with open(outputFile5, 'w') as outFile5:
    outFile5.write(seq_clean[89:110])
with open(outputFile5, 'r') as outFile5:
    outFile5_data = outFile5.read()
    print(f"The file {outputFile5} has {len(outFile5_data)} characters")

numArr1 = [9, 5, 7, 3, 12, 18]
numArr2 = []
print(numArr1)
print(numArr2)
i, j = 0, 0
while i in numArr1:
    while j in numArr2:
        if numArr1[i] < numArr1[i+1]:
            numArr2.append[i] = numArr1[i]
        else:
            continue
    j+=1
i+=1

print(numArr2)

from array import *

arr1 = array('i', [])
n1 = int(input("Enter the length of the FIRST Array: "))

for i in range(n1):
    x = int(input("Enter element in 1st Array: "))
    arr1.append(x)

print("Array 1:", arr1)

arr2 = array('i', [])
n2 = int(input("Enter the length of the FIRST Array: "))

for i in range(n2):
    x = int(input("Enter element in 1st Array: "))
    arr2.append(x)

print("Array 2:", arr2)

arr3 = array('i', [])

for i in range(n1):
    arr3.append(arr1[i])
i = 0
for i in range(n2):
    arr3.append(arr2[i])

print("Array 3:", arr3)



#from numpy import *
from array import *

Mat1 = Matrix('i', [])
n1 = int(input("Enter the length of the Array: "))

for i in range(n1):
    x = int(input("Enter %d element in the Array: " %(i+1)))
    arr1.append(x)

print("Array 1: ", arr1)


x = 0
for i in range(n1):
    if x <= arr1[i]:
        x = arr1[i]



print("Max value in the Array: ", x)
import numpy as np
import time
import sys

#Checking Memory size for List and Numpy array

S = range(1000) # Creating a List
print(sys.getsizeof(5)*len(S)) #finding the memory used by list elements

D = np.arange(1000)
print(D.size*D.itemsize) #finding the memory used by array elements


#Checking time taken by List and Numpy array

SIZE = 10000000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x,y) for x,y  in zip(L1,L2)] #finding sum of all the elements in the List
print((time.time()-start)*1000)

start = time.time()
result = A1+A2
print((time.time()-start)*1000)





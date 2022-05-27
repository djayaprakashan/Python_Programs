# Python code to demonstrate
# to find all permutation of
# a given string
 
# Initialising string
initial_string = input("Enter the String: ")
 
# Printing initial string
print("Initial string", initial_string)
 
# Finding all permutation
result = []
 
def permutation(data, i, length):
    if i == length:
        result.append(''.join(data) )
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permutation(data, i + 1, length)
            data[i], data[j] = data[j], data[i] 
permutation(list(initial_string), 0, len(initial_string))
 
# Printing result
print("Resultant permutations", str(result))
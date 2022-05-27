#List
name = ["aaa", "bbb", "ddd", "eee", "fff"]
age = [23, 43, 18]
print(name)
print(age)

print(name[3]) # print a specific index value in list
print(name[2:]) # print the values after the specified index
print(name[-1]) # print the list from last
name_age = [name, age] # Combines 2 lists to make a new list
print(name_age)

name.insert(2, "ccc") # insert an item in specified index position
print(name)


name.remove("ddd") # remove an item from the list in first occurance
print(name)

print(name.pop(1)) # remove an item from the list in specified index position
print(name[1])

name.append("ggg") # append only the item in list 
print(name)

name.extend(["hhh", "iii", "jjj"]) # extent the list by appending
print(name)

print(min(name)) # finds the minimum value in the list
print(max(name)) # finds the maximum value in the list

# can also use sum and sort functions

print(name.copy()) # returns shallow copy
print(name.index("ggg")) # return the index value of an item
print(name.count("ccc")) # return number of occurance of an item in the list

print(len(name)) # print the length of the list

new_name = name.copy() # used to create a duplicate copy of an existing list
print(new_name)



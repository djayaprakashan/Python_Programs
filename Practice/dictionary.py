myDict = {} # Creates a empty dictionary
print(myDict)

myDict = {"one": 1, 
    "two": 2, 
    3 : "three", 
    "four": 4.4
}
print(myDict)
print(myDict[3])

for key, value in myDict.items(): # print dictionary items in each line using loop
    print(key, value)

#newDict = {}
newDict = myDict.copy() # a shallow copy of D
print(newDict)

Dict3 = myDict.fromkeys("Hello") # Create a new dictionary with keys from iterable and values set to value.
print(Dict3)

print(myDict.items()) # a set-like object providing a view on dictionary items

print(myDict.keys()) # a set-like object providing a view on dictionary keys

print(myDict.values()) # an object providing a view on dictionary values

print(myDict.get(3)) # Return the value for key if key is in the dictionary, else default.

myDict.popitem() # Delete the last item in the dictionary 
print(myDict)

myDict.setdefault(5, "five") # Append only one key pair value in the dictionary
print(myDict)

myDict.update((("six",6),(7, "seven"))) # Append multiple key pair value in the dictionary
print(myDict)

myDict.clear() # Clear the dictionary
print(myDict)

keys = ['aaa', 'bbb', 'eee']
values = [23, 45, 54]
data = dict(zip(keys, values))
print(data)

data['hhh'] = 45 # adding a new key value to a dictionary
print(data)

# Creating a dictionary with dictionary and list as item
prog = {'JS':'Atom', 'CS':'VS', 'Python':['Pycharm','Sublime'], 'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(prog)
print(prog['JS'])
print(prog['Python'])
print(prog['Python'][1])
print(prog['Java'])
print(prog['Java']['JEE'])

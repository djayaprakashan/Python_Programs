myString = "This is a String."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

first = "water"
second = "fall"
third = first + second
print(third)

name = input("What is your name? " )
print(name)

color = input("What is your favourite color? ")
animal = input("What is your favourite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))

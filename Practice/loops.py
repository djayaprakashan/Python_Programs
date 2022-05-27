# While loop
import random

n = 1 
while n <= 3:
    print("I Love Python")
    n += 1

name = ["Dhana", "Kavitha", "Vedha"]

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

#for loop
for i in name: # printing from a list
    print(i)

for j in [41, 36, 31]: # list of items given in the loop itself
    print(j)

for k in ["NJ", "CA", "TX"]: # list of items given in the loop itself
    print(k)

for l in range(1,10): # list of items given as range
    print(l)

for m in range(4):
    for o in range(3):
        print(f'({m},{o})') # print the values in (1,1) form
        print((m,o))        # print the values in (1, 1) form





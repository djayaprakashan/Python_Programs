age = int(input("Enter the age: ")) # By default all the values in input is string
if age >= 18:
    print("Adult")
elif  age >= 13:
    print("Teen")
elif age > 10:
    print("Tween")
elif age >= 5:
    print("Kid")
elif age >= 2:
    print("Little kid")
else:
    print("Baby")
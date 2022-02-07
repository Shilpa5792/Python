# simple if statement

num = 3
if num > 0:
    print("statement is true")

print()
# if...else statement

num = -1
if num >= 0:
    print(num, "is positive number or zero")
else:
    print(num, "is negative number")

print()
# if...elif..else statement

num = 0

if num > 0:
    print(num, "is positive number")
elif num == 0:
    print("number is zero")
else:
    print(num, "is negative number")

print()
# nested if statement

num = float(input("Enter the number: "))
if num >= 0:
    if num == 0:
        print("number is zero")
    else:
        print("number is positive")
else:
    print("number is negative")


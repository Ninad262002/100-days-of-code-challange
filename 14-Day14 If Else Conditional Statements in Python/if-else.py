num = int(input("Enter a number: "))
if ( num < 0):
    print("the number is negative")
elif (num == 0):
    print("the number is zero")
elif (num == 999):
    print("the number is special")
else:
    print("the number is positive")
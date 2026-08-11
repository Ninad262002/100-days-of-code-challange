num = 1
if (num < 0):
    print("the number is negative")
elif (num > 0):
    if (num <= 10):
        print("the number is positive and less than or equal to 10")
    elif (num > 10 and num <= 20):
        print("the number is positive and greater than 10 and less than or equal to 20")
    else:
        print("the number is positive and greater than 20")
else: 
    print("the number is zero")

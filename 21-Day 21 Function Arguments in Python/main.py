# def average(a, b):
#     print("The average is ", (a+b)/2)

# average(4,6)

# def average(a=9, b=1):
#     print("The average is ", (a+b)/2)

# average()
# average(3, 5)

# def name(fname, mname = "john", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)
# name("ninad", "Prashant", "Mahure")

#key word argument
#variable length arguments

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        return sum/len(numbers)


c = average(5,6)
print(c)


def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchana", lname = "Barnes", fname = "james")

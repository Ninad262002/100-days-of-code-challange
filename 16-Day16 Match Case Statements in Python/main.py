x = int(input("Enter a number:"))

match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case _ if x!=90:
        print(x, "is not 90")
    case _ if  x!=80:
        print(x, "is not 80")
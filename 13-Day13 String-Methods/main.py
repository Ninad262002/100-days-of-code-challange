a = "Ninad!!!!!!!!!!!!Ninad"
print(len(a ,))
print(a.upper())


#Rstip
print(a.rstrip("@"))
print(a.replace("Ninad", "Ninad Rane"))

blogHeading = "introduction to python"
print(blogHeading.capitalize())

str1 = "Welcome to the console!!"
print(len(str1))
print(len(str1.center(50)))
print(str1.center(50))
print(a.count("Ninad"))


str1 = "Welcome to the console!!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the console!!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is")) #it will return the index of first occurrence of the substring "is" in the string str1. If the substring is not found, it will return -1.
print(str1.find("if"))


str1 = "He's name is Dan. He is an honest man."
print(str1.index("is")) #it will return the index of first occurrence of the substring "is" in the string str1. If the substring is not found, it will return -1.
#print(str1.index("if"))


str1 = "WelcomeToTheConsole1234"
print(str1.isalnum())

str1 = "WelcomeToTheConsole1234"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "we wish you a Merry Christmas and a Happy New Year "
print(str1.isprintable())

str1 = "we wish you a Merry Christmas and a Happy New Year \n"
print(str1.isprintable())

str1 = "            "  #pushing spacebar
print(str1.isspace())
str1 = "    "  #pushing tab
print(str1.isspace())


str1 = "Welcome To The Console!!"
print(str1.istitle())
str1 = "Welcome to the console!!"
print(str1.istitle())

str1 = "Python is a programming language."
print(str1.startswith("Python"))
print(str1.swapcase())




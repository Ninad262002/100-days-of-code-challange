marks = [3, 5, 6, "Ninad", True, 66, 11, 45, 67, 99, 100]
# print(type(marks))
# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[-3]) #length of marks - (-3)
# print(marks[-2]) #3-2 =1 so answer should be 5

#to find something in list
# if 7 in marks:
#     print("yes")
# else: 
#     print("No")

# print(marks)
# print(marks[1:])
# print(marks[1:-2])
# print(marks[1:8:2])

#List comprehension
# lst = [i for i in range(4)]
# lst = [i*i for i in range(4)]
# print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)
# sum is python
# a = 50
# b = 20
# sum = a+b
# print("sum of a and b is :",sum)


# arithmetic operator
# a = 5
# b = 4
# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)
# # print(a % b) use for reminder



# relational/comparison operator
# a = 40
# b = 10
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a <= b)
# print(a >= b)


#assignment operator 
# num = 10
# num += 20
# num -= 20
# num *= 20
# num /= 20
# num %= 20
# print(num)

 
#logical operator
# val1 = True
# val2 = False
# print(val1 and val2) beause both are not the same(False) 
# print(val1 or val2)  beause one is true (True)
# print(val1 not val2) (not will always give opsite ANS)so its is false

# type conversion OR type casting 
# a = int("3")
# b = 4.28

# sum = a+b
# print(type(a))
# print(type(b))
# print(sum)

# Input in python 

# name = input("enter your name :")
# age = float(input("enter your age :"))
# marks = int (input("enter your marks :"))

# print(name)
# print(type(age),age)
# print(type(marks),marks)

# practice question (write a parogram to input two number and print sum)
# first = int(input("enter first number :"))
# second = int(input("enter second number :"))

# print("sum :",first + second)

# practice questuon (write a parogram to input a size of square and print the area )
# side = float(input("area are :"))

# print(side*side)

# # practice question (write a parograme input 2 floating point number and print thier average)
# float1 = float(input("first number :"))
# float2 = float(input("second number :"))


# print("average is :", (float1 * float2)/2)

# pracice question 

# first = int(input("enter a number :"))
# second = int(input("enter a number :"))

# print(first >= second)

# LECTURE:2
# string and conditional statment 
# CONCATENATION 

# str1 = "my name is zabihullah"
# str2 = "i live in rustam"
# finalstr = str1 + str2
# print(finalstr)


# FINDing lenght of STR

# str1 = "zabihullah"
# print(len(str1))
# str2 = "apnacollage"
# print(len(str2))
# print(str1)
# print(str2)
# final = str1 + str2 
# print ( final)

# slicing in python
# str = "zabih ullah"
# print(str[ 2 :7])

# negative slicing in python
# str = "zabihkhan"
# print(str[-5 : -1])

# string function in Python

# str = "i am studing python from apna collage"
# print(str.endswith("apna collage")) return true if string end with substring
# print(str.capitalize()) its capitalize first letter of string
# print(str.replace( "i am studing python from apna collage"," i am a coder" )) replace all occurrence of old with new
# print(str.find("t")) return 1st index of first world and tell you the index of letter 
# print(str.count("m")) count the accurrence of sub str in string


# practice question(write a parogram to input user first name and print its  length) 
# name = input("Enter your name :")
# print(name)
# print(len(name))

# practce question(write a parogram to find the letter of $ in string)
# find =" hi$, my name$ is zabih$ "
# print(find.count("$")) output (3) 


# conditional satatment 

# light = "yellow"

# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("waiting")

# age = 20
# if(age >= 18):
#     print("can vote")
#     print("can also drive and applay for licens ")
# elif(age <= 18):
#     print("you are under age and can not vote and applay for licens")

# num = 5 

# if(num > 2):
    # print("grater than 2")
# if(num > 3):
#     print("grater than 3") 
# elif(num > 3 ):
    # print("grater than 3")
# (the moment if is given false then elif will run and if (if statment) are true then it will not give false)      

# if-elif-else

# light = ""

# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("looking")
# else:
#     print("system is broken")


# # pratice question (find the grade of student)
# marks = int(input('Enter marks :'))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# elif(marks >= 60 and marks < 70):
#     grade = "D"
# else:
#     grade = "fail"
# print("grade of student is :",grade)

# nesting in funtion (write statment OR function  in one another)
# age = int(input("enter age :"))
# if(age >= 18):
#     if(age >= 80):
#         print("can not drive")
#     else:
#          print("can dive")
# else:
#     print("can not drive")
# 

# practice question (write a parograme to check if the number from user is odd are even)
# num = int(input("Enter a number :"))
# if(num%2 == 0 ):
#     print("this is Even number")
# else:
#     print("this is Odd number")



# pactice question (WAP to find the greatest of 3 number enter by the user)
# first = int(input("Enter number :"))
# second =int(input("Enter number :"))
# third = int(input("Enter number :"))
# if (first >=second and first  >= third):
#     print("first number is greater")
# elif(second >= third):
#     print("Second number is greater")
# else:
#     print("Third number is greater")


# practice question (write a parograme to check if the number is multipule of 7)

# multi = int(input('Enter a number :'))

# if(multi % 7 == 0 ):
#     print("number is multipul of : 7")
# else:
#     print("not multipiule of : 7")
    
# list in Python

# marks = [55,65,78,44,50]
# print(marks[4])
# print(type(marks))
# print(len(marks))

# student = ["zabih",70, 20, "rustam"]
# print(student)

# sliceing in python
# num = [44,55,44,23,30,67,78,89,90,12,34,20]
# print(num[ 2:6 ])

# list method 
# list = [ 2,4,5,1,3,5,7,]
# list.append(23)
# print(list)

# list = [3,2,1,5,4,6]
# list.sort()
# list.sort(reverse=True)
# list.reverse()
# list.insert(2,10)
# list.remove(2)
# list.pop(4)
# print(list)

# Tuples in python(a bulit in type that help us write immutable code ) 
# tup = (22,34,12,23)
# print(tup)
# print(type(tup))

# # pratice question (warite a parogram to ask the user name their 3 favorite videogames )
# games = []
# gam1 = input("enter name of favorite game :")
# gam2 = input("enter name of favorite game :")
# gam3 = input("enter name of favorite game :")
# games.append(gam1)
# games.append(gam2)
# games.append(gam3)
# print(games)




# practce question (write a parogram to check if the list contain a palindrome element )
# TO check if the value is palindrome 
# list1 = [1,2,3,2,1]
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if(copy_list1 == list1):
#     print("palandrome")
# else:
#     print("Not palandrome") 
# list3 = [1,2,3,2,1]
# list3.reverse()
# print(list3)

# pratice question (write a parograme to count the number of student with a grade in the following tuple)
# grade = ["C","D","A","A","B","A"]
# print(grade.count("B"))   
# grade.sort()
# print(grade)































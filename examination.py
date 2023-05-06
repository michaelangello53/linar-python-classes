#1a)Create a variable called "age" and assign it the value 25. Print the value of the variable. 
age=("25")
print(age)
#1b) What is the difference between an integer and a floating-point number in Python? Provide an example for each
'''a float is represented by a number why an integer is represented by alphabets.....example of a float(1,3),example of an integer(hello)'''


#2a) Write a Python program that adds two numbers together and prints the result.
num1=float(input("enter first number:"))
op=input("enter the operation:")
num2=float(input("enter second number"))



if op=="+":
   print(num1 + num2)

#b) Write a Python program that takes a number as input and multiplies it by 10. Print the result
def multiplyNum(num1):
    return num1 * 8

result = multiplyNum(8)
print(result)

#3a) Write a Python program that checks if a number is even or odd. If the number is even, print "Even", otherwise print "Odd"
def num():
    numbers=["1","2","3","4","5","6"]
    for odd_numbers in numbers:
        print(odd_numbers)


num()        


#3b) Write a Python program that takes a number as input and checks if it is positive, negative, or zero. Print the result.
def numbrs():
    numb=int(input("Input number:"))
    if numb==1:
      print(f'the number is negative')
    if numb==2:
        print(f'the number is positive')
    if numb==3:
        print(f'the number is negative') 
    if numb==4:
        print(f'the number is positive')
    if numb==5:
        print(f'the number is negative') 
    if numb==6:
        print(f'the number is positive')
    if numb==7:  
        print(f'the number is negative')   
    if numb==8: 
        print(f'the number is positive') 
               

    else:
        print('invalid number')    
numbrs()



#4a) Create a list of numbers from 1 to 10. Print each number in the list using a loop
def num():
    numbers=["1","2","3","4","5","6","7","8","9"]
    for odd_numbers in numbers:
        print(odd_numbers)

num()        


#4b) Write a Python program that takes a list of numbers as input and returns the sum of all the numbers in the list.


















#5a) Write a Python function that takes two numbers as input and returns their sum
def addNum(num1, num2):
    print(num1 + num2)
addNum(2, 4)

#5b) Write a Python function that takes a list of numbers as input and returns the average of all the numbers in the list.










#7a) Install and Import the "math" module and use its "sqrt" function to calculate the square root any number
import math 
math.sqrt(10)
print("answer....")








#7b) Install and Import the "random" module and use its "randint" function to generate a random number between 1 and 10 
import random as ran
ran.randint(1,11)












#7c) Install and Import the "pywhatkit" module and use its "whatsapp" function to send a DM to your tutor with the body “Good Day Sir”
import pywhatkit as pwk
pwk.sendwhatmsg_instantly("+2349023459712","Good day sir",5,False)
print("sending.....")



#10) Give a feedback on this Python course, your instructor and this examination
"""python course is a nice course,i really enjoyed every of the class.The instructor is really e good teacher,i love the way he teaches and 
carry all his students along when teaching.For the examination i really dont have anything to say """





def Average(l): 
    avg = sum(l) / len(l) 
    return avg
  
my_list = [2,4,6,8,10] 
average = Average(my_list) 
  
print("Average of my_list is", average)



num = int (input ( "Enter any number to test whether it is odd or even:"))

if (num % 2) == 0:

              print("The number is even")

else:

              print ("The provided number is odd")

num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")        



def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,23]))         

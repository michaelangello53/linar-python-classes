my_dict={"a": 1,"b": 2,}
for key,value in my_dict.items():
    print(key,value)





def my_function(*args,b=2):
    results=(all (args),b)
    return sum(results)==b

print(my_function(7,6,7,0,b=6))


def modify_str():
    str1="i love python"
    str1.replace("love","enjoy").split()
    return str1
print(modify_str())




def my_func(x):
    if x==0:
        return 0
    else:
        return x + my_func(x-1)
    
print(my_func(5))    
      


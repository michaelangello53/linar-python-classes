a="michael linear"
print(a.center(150))
b="hello michael linear"
print(b.endswith("."))
c="My name is {fname}, I'm {age}".format(fname = "michael", age = 20)
print(c.format())
d='hellomichaellinear'
print(d.isalnum())
e="\u0030"#unicode for 0
print(e.isdecimal())

print(a.islower())
g="   "
print(g.isspace())
h=("michael","linear")
print(" ".join(h))
strTostrip="strStrip"
print("before strip:",strTostrip)
print("after strip:",strTostrip.lstrip())

  
string1 = "Welcome to python 3.9"
print("Original String 1 : ", string1)
  
# suffix exists
result = string1.removesuffix("3.9")
print("New string : ", result)
  

greetings="hello,michael linear"
r=greetings.rfind("e")
print(r)

school="i love going to linear'linear is my favorite place"
m=school.rpartition("linear")
print(m)
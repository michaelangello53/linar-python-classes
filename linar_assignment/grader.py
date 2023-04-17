def grade(m,e,p,c,b):
    gradesum = m + e +p+c+b
    return gradesum
stpercent1 = ((grade(80,69,70,60,51)/500)*100)
stpercent2 = ((grade(66,90,74,61,57)/500)*100)

print("Segun had " + str(stpercent1)  + " percent and micheal had " + str(stpercent2)) # Using the str function

print(f'Segun had {stpercent1} percent and micheal had {stpercent2}') #F-string

print("Segun had {} percent and micheal had {}".format(stpercent1,stpercent2)) #Using the format methos


print(grade(80,69,70,60,51))
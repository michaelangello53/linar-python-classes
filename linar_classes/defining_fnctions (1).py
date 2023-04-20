'''def vehicle(weight_in_kg):
    weight = int(weight_in_kg[0:-2])
    if 10>=weight>=100:
        print(f'Youre vehicle weighs {weight}kg and will have 2 tyres. ')
    elif 150>=weight>=101:
        print(f'Youre vehicle weighs {weight}kg and will have 3 tyres. ')
    elif 800>=weight>=151:
        print(f'Youre vehicle weighs {weight}kg and will have 4 tyres. ')
        
print("Welcome!!!\nLets help you calculate your number of tires.")
weight_in_kg = input('What is the weight of your vehicle in Kg? eg 100kg\n')
vehicle(weight_in_kg)'''

'''Testing approximation  function'''

'''num=str(input('Enter your number: '))
1.2 
def appx(num):
    appnum=(float(num[0])+1)
    return appnum
if 9>=int(num[2])>=5:
    print(f'Answer is {appx(num)}')
elif 5>int(num[2])>=0:
    def lappx(num):
        loappx=(float(num[0]))
        return loappx
    print(f'Answer is {lappx(num)}')'''

#Make it that if strings are used it will request for numbers
'''num=input('Enter your number: ')
numbers=int(num)
if numbers!=str():
    print('Pls use only numbers')
else:
    print('Lets continue')'''

'''a='Segun Ola'
print(a[-3:])
print(a[6:])
print(a[6:9])
print(a.index('l'))'''

'''a=input('Enter your full name\nSurname first: ')
first_name=a[-3:]
surname=a[0:5]
print(f'Mr {surname}, Welcome here and Thanks.\nHey {first_name}, are you satisfied?\n'
      f'My greetings to the family of {surname} ')'''

'''
def appx():
    appnum=(float(wh)+1)
    return appnum

def lappx():
    loappx=(float(wh))
    return loappx

a='Segun Ola'
Sn,Fn=a.split(' ')
print(Sn)
print(Fn)
a=input('Input a decimal: ')
wh,dec=a.split('.')
if 9>=int(dec[0])>=5:
    print(print(f'Answer is {appx()}'))
elif 5>int(dec[0])>=0:
    print(print(f'Answer is {lappx()}'))
'''
a='Post Malone'
Sn,Fn=a.split(' ')

print(f'Mr {Sn}, Welcome here and Thanks.\nHey {Fn}, are you satisfied?\n'
 f'My greetings to the family of {Sn}\n\n ')

b='Ed Sheeran'
rn,dn=b.split(' ')

print(f'Mr {rn}, Welcome here and Thanks.\nHey {dn}, are you satisfied?\n'
 f'My greetings to the family of {rn}\n\n ')

c='Saint jhn'
Surname,First=c.split(' ')

print(f'Mr {Surname}, Welcome here and Thanks.\nHey {First}, are you satisfied?\n'
 f'My greetings to the family of {Surname} \n\n')

d='Post Malone'
last,Frst=d.split(' ')

print(f'Mr {last}, Welcome here and Thanks.\nHey {Frst}, are you satisfied?\n'
 f'My greetings to the family of {last} ')
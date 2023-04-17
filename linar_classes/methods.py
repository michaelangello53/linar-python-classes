a = "segun ola"

print(a.capitalize())
print(a.upper())
print(a.lower())
b = input("Enter your gmail: ")
checking = b.endswith('@gmail.com')
if checking == False:
    print("Enter a corret gmail")
else:
    print("Thanks for inputting your gmail")

print(a.center())
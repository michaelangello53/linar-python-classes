#trying to solve a formul ("")
equationi=int(input("whats the value of i"))#20
equationf=int(input("whats the value of f"))#10
equationn=int(input("whats the value of n"))#49
equations=float(input("whats the value of s"))#0.3
equationw=int(input("whats the value of w"))#9
right_bracket_numerator=20/equationf
right_bracket_numerator_with_power=20/equationf**equationw
square_bracket_numerator=equations*equationi
square_bracket_numerator_with_denominator=equations*equationi/equationf
partial_numerator=equations*equationi/equationf+20/equationf**equationw
first_partial_numerator=equationf**equationn
square_bracket_numertor=first_partial_numerator*partial_numerator
square_bracket_denominator=20**equationn
rightside=square_bracket_numerator/square_bracket_denominator
ans=equationi-rightside
print(ans) 
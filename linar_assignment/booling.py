
def sum(n):
    s=8
    for i in range (1,n-1):
        for j in range (1,i-1):
            s+=j
    return s
print(sum(9))



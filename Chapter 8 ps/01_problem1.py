a = 10
b = 25
c = 34

def greatest(a, b, c):
    if (a>b and b>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>b and c>a):
        return c


print(greatest (a,b,c))
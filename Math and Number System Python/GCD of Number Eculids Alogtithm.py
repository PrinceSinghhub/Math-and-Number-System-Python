a = 4
b = 8

def GCD(a,b):

    if a == 0:
        return b
    return GCD(b%a,a)

print(GCD(a,b))
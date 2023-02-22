a = 7
b = 5

def HCF(a,b):
    if a == 0:
        return b
    return HCF(b%a,a)

def LCM(a,b):

    return int((a*b)/HCF(a,b))
print(LCM(a,b))
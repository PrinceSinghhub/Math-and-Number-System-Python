def primeOrNot(n):

    res = True
    c = 2
    while c*c <= n:
        if n%c == 0:
            res = False
            break
        c+=1

    if res:
        print("Prime Number",n)
    else:
        print("Not a Prime Number")

for i in range(2,11):
    primeOrNot(i)
def ApowerB(base,power):

    ans = 1
    while power > 0:
        if((power & 1)==1):
            ans *= base

        base *= base
        power = power >> 1

    return ans

print(ApowerB(3,3))



def magicNumber(n):
    ans = 0
    base = 5
    while n > 0:
        last = n&1
        n = n>>1
        ans = ans + last * base
        base = base*5

    print(ans)

magicNumber(3)

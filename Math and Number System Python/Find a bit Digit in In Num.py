import math as m
def CountBit(n):
    base = 2
    ans = int(m.log(n)/m.log(base)+1)
    print(ans)

CountBit(10)
def XOR(i):
    if i % 4 == 0:
        return i
    elif i % 4 == 1:
        return 1
    elif i % 4 == 2:
        return i+1
    elif i % 4 == 3:
        return 0
a = 13
b = 5
ans = XOR(b) ^ XOR(a-1)
print(ans)

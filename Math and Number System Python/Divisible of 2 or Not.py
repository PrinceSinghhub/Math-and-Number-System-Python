def DivorNot(n):
    res = n&(n-1)
    if res == 0:
        return True
    return False


print(DivorNot(16))

for n in range(1,21):
    res = n & (n - 1)
    if res == 0:
        print(n)

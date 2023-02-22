def even_or_old(n):
    if (n & 1) == 1:
        return False
    else:
        return True

ans = even_or_old(15)
print(ans)
print(16 | 1)
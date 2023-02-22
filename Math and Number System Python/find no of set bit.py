def findNum(n):

    count = 0
    while n>0:
        count+=1
        # n = n - (n&(-n)) also write like that
        n = n&(n-1)

    return count

print(findNum(7))
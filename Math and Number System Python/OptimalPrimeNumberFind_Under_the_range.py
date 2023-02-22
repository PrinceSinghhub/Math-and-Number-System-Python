def FindPrime(n):

    myarr = [False]*n
    print(myarr)


    i = 2
    while i*i<=n:
        if myarr[i] == False:
            j = i * 2
            while j < n:
                myarr[j] = True
                j += i
        i+=1

    print(myarr)

    for i in range(2,n):
        if myarr[i] == False:
            print(i,end=" ")

FindPrime(40)
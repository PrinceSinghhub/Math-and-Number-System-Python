def findallXOR(a):
    for i in range(a):
        if i%4 == 0:
            print(i)
        elif i%4 == 1:
            print(1)
        elif i%4 == 2:
            print(i+1)
        elif i%4 == 3:
            print(0)


findallXOR(10)
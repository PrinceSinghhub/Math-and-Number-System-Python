import math as m
def OptimalFactore(n):

    start = 1
    arr = []
    while start<=m.sqrt(n):

        if(n%start==0):
            if(n/start == start):  # for ignore the dublicate value
                print(start,end=" ")

            else:
                # print(start,int(n/start), end=" ")  not a sorted manner thats why creat  a list
                print(start,end=" ")
                arr.append(int(n/start))

        start+=1
    arr.sort()
    for i in arr:
        print(i, end=" ")


OptimalFactore(17)

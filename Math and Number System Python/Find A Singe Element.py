def findElement(arr):
    unique = 0
    for i in arr:

        unique = unique ^ i
    print(unique)

arr=[1,2,1,2,5]
findElement(arr)

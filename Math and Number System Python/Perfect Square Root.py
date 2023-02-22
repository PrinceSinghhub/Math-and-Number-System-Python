def PerfectSquareRoot(n):

    start = 0
    end = n

    while(start<=end):

        mid = int(start+(end-start)/2)
        if(mid*mid == n):
            print(mid)
            break
        if (mid*mid>n):
            end = mid-1

        if (mid*mid<n):
            start = mid+1



PerfectSquareRoot(49)
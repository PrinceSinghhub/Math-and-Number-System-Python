def FloatPerfectSquare(n,decimalPlace):

    ans = 0.0
    increment = 0.1
    for i in range(decimalPlace):

        while (ans * ans <= n):
            ans += increment

        ans -= increment
        increment /= 10
    print(format(ans, ".3f"))

FloatPerfectSquare(40,3)
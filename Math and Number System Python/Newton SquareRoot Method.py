import math as m
def NewtonMethod(N):

    X = N
    root = None

    while(True):
        root = 0.5 * (X+N/X)   # (X+N/X)/2 also write

        if(m.fabs(root-X)<1):
            break

        X = root

    print(format(root,".3f"))


NewtonMethod(40)
def fib_series(n):
    if (n==0):
        return 0
    else:
        n1,n2 = 1,1
        for i in range(n-1):
         n1,n2 = n2,n1+n2
        return n1

def last_8(x):
    return str(x)[-8:]

print(last_8(fib_series(5)))

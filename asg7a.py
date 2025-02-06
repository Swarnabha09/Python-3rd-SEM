#nth term of the series

def fibo(n):
    a=0
    b=1
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("enter numbers:"))
print(fibo(n))

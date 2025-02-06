#fibonacci series

def fibo(a=0,b=1,term=1):
    if term>0:
        print(a)
        fibo(b,a+b,term-1)

n=int(input("enter the number:"))
fibo(term=n) #as a and b have allocated a default value, so when we're calling we're not mentioning them...

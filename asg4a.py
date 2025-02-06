#fibonacci series
n=int(input("enter range:"))
a=0
b=1
if n<=0:
    print("invalid input")
else:
    for i in range(1,n+1):
        if n==1:
            print(a)
        else:
            print(a,end=' ')
            a,b=b,a+b

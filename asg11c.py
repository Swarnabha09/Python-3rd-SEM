n=int(input("enter num:"))
a=0
b=1
f1=open("fibo.txt","w")
while a<=n:
    f1.write(str(a)+'\n')
    a,b=b,a+b
f1.close()

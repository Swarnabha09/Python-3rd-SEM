def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
f1=open("Prime_num.txt","w")
n=int(input("how many numbers:"))
b=[]
i=2
while len(b)<n:
    if isPrime(i):
        b.append(i)
    i+=1
for i in b:
    f1.write(str(i)+"\n")
f1.close()

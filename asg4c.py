#automorphic numbers
n1=int(input("start:"))
n2=int(input("end:"))
for i in range(n1,n2+1):
    if i==(i**2)%(10**len(str(i))):
        print(i)
    

n=int(input("enter lines:"))
for i in range(n):#(0),(1),(2),(3),(4)
    print(" "*(n-i),end="")
    for j in range(i+1,0,-1):#(1),(2,1),(3,2,1),(4,3,2,1),(5,4,3,2,1)... gap=-1
        print(chr(j+64),end="")#(64+1=A),(64+2=B),(64+3=C),(64+4=D),(64+5=E)
    print()

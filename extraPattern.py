n=int(input("number of lines:")) #for input n=5
for i in range(n):#0 to n-1=(5-1)=4 total 5 iterations
    print(" "*(n-i-1),end="")#space triangle (5-0-1)=4,(5-1-1)=3,...,(5-4-1)=0 space
    print("*"*(2*i+1),end="")#triangle... (2*0+1)=1, (2*1+1)=3,..., (2*4+1)=9 stars
    print()#for next line

for i in range(n-2,-1,-1):#reversing...(n-2)=3 to -1...total 4 times iteration
    print(" "*(n-i-1),end="")#(5-3-1)=1,(5-2-1)=2,...,(5-0-1)=4 space
    print("*"*(2*i+1),end="")#(2*3+1)=7,(2*2+1)=5,...,(2*0+1)=1 stars
    print()#for next line


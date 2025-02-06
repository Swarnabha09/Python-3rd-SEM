n=int(input("i/p="))
for i in range(n):
    print(" "*(n-i-1),end=' ')
    print('*',end=' ')
    for j in range(1,2*i-1):
        print(" ",end=" ")
    print("*")
    print()
    

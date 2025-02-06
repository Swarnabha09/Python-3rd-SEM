n=int(input("enter:"))
for i in range(n):
    print(" "*(n-i-1),end="")
    print(chr(65+i),end="")
    if i>0:
        print(" "*(2*i-1),end="")
        print(chr(65+i),end="")
    print()

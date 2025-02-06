n=int(input("lines:"))
for i in range(2*n):
    if i<n:
        print("*"*i)
    elif i==n:
        print("*"*(2*i-1))
    else:
        print(" "*(i-1)+"*"*(2*n-i))
        
        

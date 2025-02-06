import numpy as np
m=int(input("enter number of rows:"))
n=int(input("enter number of columns:"))
a=np.matrix(eval(input(f"enter {m}X{n} matrix:")))
b=np.random.randint(1,20,size=(n,m))
print(a)
print(b)
c=np.matmul(a,b)
print(c)

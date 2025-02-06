s=input("enter a string:")
l=0
u=0
for i in s:
    if i.isupper():
        u+=1
    if i.islower():
        l+=1
print("uppercase=",u)
print("lowercase=",l)

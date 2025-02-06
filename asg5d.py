s=input("enter a string:")
r=input("enter range:")
a=int(r.split()[0])
b=int(r.split()[1])
x=s[a:b+1]
print(x)
if x==x[::-1]:
    print("palindrome")
else:
    print("not palindrome")

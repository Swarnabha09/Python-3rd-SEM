s=input("enter:")
l=list(map(int,s.split()))
#map function is used to convert elements of the list s.split() and then make a list with these integers named 'l'
print(l)
l1=[0]*(sorted(l)[-1]+1)
print(l1)
for i in l:
    l1[i]=i
print(l1)

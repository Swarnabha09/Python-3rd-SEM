s=input("enter:")
l=list(s.split())
#l=list(map(int,l))
l=[int(i) for i in l] #list comprehension
#we can use either map function or list comprehension method
print(l)
smax=sorted(l)[1]
smin=sorted(l)[-2]
print(sorted(l))
print(l)
print(smax,smin)

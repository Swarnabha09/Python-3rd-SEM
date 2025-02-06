#sets are a type of data structure having unique elements, these are mutable

s1=input("enter 1st statement:")
s2=input("enter 2nd statement:")
st1=set(s1.split())
st2=set(s2.split())
print(st1.intersection(st2))
print(st1.union(st2))
print(st1-st2)

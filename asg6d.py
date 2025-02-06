#dictionary is a combination of keys and values,each keys has to be unique,these are mutable,Values are accessed via keys.

s=input("enter string:")
d={}
for i in s.split():
    d[i]=s.split().count(i)#allocation of keys and values
print(d)

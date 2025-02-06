'''
no. of lines
word count
frequecy of word
'''

'''
re.sub(pattern, repl, string):
#Replaces all occurrences of the pattern in the string with a new string.

result = re.sub(r'\d+', 'number', 'abc 123 def 456')
print(result)  # abc number def number

'''
from collections import Counter
import re
f1=open("text.txt","r")
r=f1.read()
r1=re.sub(r'[^\w\s]','',r).lower()
print(r1)
count=Counter(r1)
print("Word count=",count)





f1.seek(0)
unique=[]
for i in r1.strip().split():
    if i not in unique:
        unique.append(i)
for i in unique:
    print(i,'->',r1.split().count(i))

f1.seek(0)
r1=f1.readlines()
c=0
for i in r1:
    if i=='\n':
        c+=1
print("number of lines:",c+1)

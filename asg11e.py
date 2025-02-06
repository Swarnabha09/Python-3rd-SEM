import os
f1=open("read1.txt","r")
f1.seek(0)
print(len(f1.read()),"bytes")
print(os.path.getsize("read1.txt"),"bytes")
f1.close()

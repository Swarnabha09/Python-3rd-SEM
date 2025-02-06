class F:
    def __init__(self,n):
        self.v=n
    def __add__(self,other): #operator overloading for '+'
        return self.v+other.v
    def __sub__(self,other): #operator overloading for '-'
        s=""
        for i in self.v:
            if i not in other.v:
                s+=i
        return s

ob1=F("Swarnabha")
ob2=F("Ghosh")
print(ob1+ob2)
print(ob1-ob2)

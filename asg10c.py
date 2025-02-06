#super class
class B:
    def __init__(self,a:int):
        self.val1=a
        print("B object created")
    def show(self):
        print("Showing class B")

#subclass
class C(B):
    def __init__(self,a:int,b:int):
        super().__init__(a)
        self.val2=b
        print("C object created")
    def show(self):
        print(f"showing C class with {self.val1} and {self.val2}")

c=C(10,11)
c.show()

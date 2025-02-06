class B:
    def __init__(self,val):
        print("Class B object created")
        self.val=val
    def show(self):
        print(f"Showiong Class B object having value {self.val}")

b=B(10)
b.show()
print(b)

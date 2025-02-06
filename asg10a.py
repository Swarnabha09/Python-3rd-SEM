class A:
    def __init__(self):
        print("class A object created")
    def show(self):
        print("showing class A")
    def __del__(self):
        print("class A deleted")

a=A()
a.show()
del a
#print(a)

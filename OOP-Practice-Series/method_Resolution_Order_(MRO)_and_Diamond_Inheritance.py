class A:
    def show(self):
        print("A class method called")

class B(A):
    def show(self):
        print("B class method called")

class C(A):
    def show(self):
        print("C class method called")

class D(B, C):
    pass

# Create object of D
d = D()

# Call show method
d.show()

# Print MRO
print(D.__mro__)

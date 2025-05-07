class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Initial factor set karte hain

    def __call__(self, number):
        # __call__ method jo number ko factor se multiply kare
        return number * self.factor
    
# Multiplier object banaya, factor 5 set kiya
multiplier_obj = Multiplier(5)

# Checking if the object is callable using callable() function
print(callable(multiplier_obj))  

# Object ko function ki tarah call karke multiply karna
result = multiplier_obj(10)  
print("Result:", result)  

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        # Getting the price
        return self._price

    @price.setter
    def price(self, value):
        # Setting the price, with validation if needed
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    @price.deleter
    def price(self):
        # Deleting the price
        print("Price is being deleted!")
        del self._price
# Create a Product object with initial price
product = Product(100)

# Accessing the price using the getter
print("Initial Price:", product.price)  # Using @property

# Updating the price using the setter
product.price = 150  # Using @price.setter
print("Updated Price:", product.price)

# Attempt to set a negative price (which is invalid)
product.price = -50  # Should print an error message

# Deleting the price using deleter
del product.price  # Using @price.deleter

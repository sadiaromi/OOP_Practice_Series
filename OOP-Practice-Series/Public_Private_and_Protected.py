class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable
        self.__ssn = ssn        # Private variable

    def show_details(self):
        print("Inside class:")
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)

emp = Employee("Sadia", 50000, "123-45-6789")

# Accessing variables
print("Outside class:")
print("Name:", emp.name)        # ✅ Public - accessible
print("Salary:", emp._salary)   # ⚠️ Protected - accessible but not recommended

# ❌ Private - will raise AttributeError
try:
    print("SSN:", emp.__ssn)
except AttributeError as e:
    print("SSN: Cannot access directly! ->", e)

# ✅ Accessing private variable using name mangling
print("Accessing private via name mangling:")
print("SSN:", emp._Employee__ssn)

# Calling method from inside the class
print("\nCalling method inside class:")
emp.show_details()

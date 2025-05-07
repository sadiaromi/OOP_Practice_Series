# Step 1: Employee class
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee Name:", self.name)

# Step 2: Department class (aggregation)
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # aggregation: storing reference to external Employee object

    def show(self):
        print("Department Name:", self.dept_name)
        self.employee.show()  
        
# Creating Employee object independently
emp1 = Employee("Sana")

# Creating Department object and passing employee reference
dept1 = Department("Software", emp1)

# Show department and employee info
dept1.show()

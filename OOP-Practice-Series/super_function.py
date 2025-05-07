# Parent class
class Person:
    def __init__(self, name):
        self.name = name

# Child class inheriting Person
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # calling Person's constructor
        self.subject = subject

    def display(self):
        print("Teacher Name:", self.name)
        print("Subject:", self.subject)

teacher1 = Teacher("Sana", "Computer Science")

# Displaying details
teacher1.display()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks Obtained:", self.marks)

student1 = Student("Sadia", 92)

student1.display()

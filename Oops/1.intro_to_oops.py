# Introduction to Object-Oriented Programming (OOP)
   # it is a programming approach that organizes code into objects, which are instances of classes. OOP allows for better code reusability, modularity, and maintainability. 

# if we take an example of student data, in simple python we can create a list of students and their details, 
# but as the data grows, it becomes difficult to manage. OOP allows us to create a class for students, which can have attributes like name, age, and grade, 
# and methods to perform operations on those attributes.

class Student:
    def __init__(self, name, age, grade, marks):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks  # Instance variable to store marks

    def display(self):
        print("name: ", self.name)
        print("age: ", self.age)
        print("grade: ", self.grade)
        print("marks: ", self.marks)


student1 = Student("Alica", 24, 12, 84)
student1.display()

student2 = Student("Julie", 23, 11, 78)
student2.display()


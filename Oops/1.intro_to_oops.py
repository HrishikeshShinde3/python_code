# Introduction to Object-Oriented Programming (OOP)
   # it is a programming approach that organizes code into objects, which are instances of classes. OOP allows for better code reusability, modularity, and maintainability. 

# if we take an example of student data, in simple python we can create a list of students and their details, 
# but as the data grows, it becomes difficult to manage. OOP allows us to create a class for students, which can have attributes like name, age, and grade, 
# and methods to perform operations on those attributes.

class Student:  # class is blueprint of object
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

print("----------")

student1 = Student("Alica", 24, 12, 84)  # object
student1.display()
print("----------")

student2 = Student("Julie", 23, 11, 78)  # object
student2.display()
print("----------")

student3 = Student("John", 25, 12, 90)   # object
student3.display()


# self and __init--

# self → Refers to the current
# object (instance) of the class.

# __init__() → An initializer method that runs automatically when an 
# object is created. It initializes the object's attributes.
#In everyday Python discussions, people often call __init__() the constructor.
print("----------")

class Employee:
    def __init__(self, name, department, salary):
        self.name = name                    # self refers to current object
        self.department = department        # self refers to current object
        self.salary = salary                # self refers to current object
                                            # after it goes into __init__
# instance variable                                            
    # above name , dept and salary are instance variable 
    # because they belongs to individual objects

# class variable

 
    def display(self):
        print("name", self.name)
        print("department", self.department)
        print("salary", self.salary)


emp1 = Employee("Hrishikesh", "Fullfilment", 40000)
emp1.display()
print()
print(emp1.salary)
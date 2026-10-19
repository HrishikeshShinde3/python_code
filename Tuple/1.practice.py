
# tuple is collection of mix data types

# Tuple = (1,2,3,4,5)

# Tuple = ('Apple', 'Banana', 'Cherry)

# Tuple = (1, 2, 'Cherry', 8.75)

My_Data = ('Hrishikesh', 24, 2.74,True)


print(My_Data[:3])   # it print 0 to 2nd index entries
print(My_Data[2:])   # it print all from 2nd index
print(My_Data[::-1]) # it reversed the tuple

employee = ("Rahul", 25, "Developer", 45000)

name, age, role, salary = employee 

print("Employee name is :", name)
print("Employee age is :", age)
print("Employee role is :", role)
print("Employee salary is :", salary) 

print(len(employee))
print(employee.count(25))

print()

employee_list = ["Rahul", 25, "Developer", 45000]
employee_tuple = ("Rahul", 25, "Developer", 45000)

print(employee_list)
print(employee_tuple)
print()

employee_list.insert(0, "Sahil")
print(employee_list)

employee_list.append("Pune")
print(employee_list)

print()
print()

employee = ( "EMP101", "Rahul", ["Python", "SQL"])
employee[2].remove("SQL")
print(employee)

print()

employee[2].append("MpngoDB")
print(employee)







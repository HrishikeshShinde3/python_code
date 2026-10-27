# Dictionary is collection of key and value pair

# Record:
#  student_name : "Alex Hales"
#  student_age : 28
#  city_name : "Edgabaston"
#  marks : 76

student = {
   "name" : "Alex Hales",
   "age" : 28,
   "city" : "Edgabaston",
   "marks" : 76,
   
}

print(student)

# key must be unique 
# values can be strings, integers, lists, tuples or even other dictionaries
# dictionaries are mutable

print(student.get("name"))
print(student.get("salary")) # returns none when key is not in dictionary

student["salary"] = 35000 # we can add key value
student["marks"] = 82 # we can update existing data using key
print(student)
del student["city"] # we can delete a data by key
print(student)

print()
print("-----Employee Data-----")

employee = {
    "name" : "Rahul",
    "age" : 25,
    "role" : "Python Developer",
    "salary" : 35000
}

print(employee["name"])
print(employee["salary"])

employee["city"] = "Pune"
print(employee)

employee["salary"] = 40000
print(employee) 


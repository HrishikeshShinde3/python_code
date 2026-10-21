
students = {
    "S101": {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    },
    "S102": {
        "name": "Priya",
        "age": 21,
        "marks": 92
    },
    "S103": {
        "name": "Amit",
        "age": 19,
        "marks": 67
    }
}

#print(students["S101"]["name"])
#print(students["S101"]["marks"])

# update the marks
students["S101"]["marks"] = 90

# add new field
students["S101"]["city"] = "Pune"

# add new student
students["S104"]={
            "name": "Sam",
            "age": 19,
            "marks": 93
        
}

#looping through the nested dictionary
# and printing the details from it

for student_id, details in students.items():
    print("Student id :", student_id)
    print("Name :",details["name"])
    print("Marks :", details["marks"])
    print("------------")


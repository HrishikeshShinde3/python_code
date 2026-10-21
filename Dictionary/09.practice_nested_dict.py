students = {
    "S101": {"name": "Rahul", "marks": 85},
    "S102": {"name": "Priya", "marks": 92},
    "S103": {"name": "Amit", "marks": 67},
    "S104": {"name": "Sneha", "marks": 78},
    "S105": {"name": "Neha", "marks": 92}
}

# print the details using the loop

for student_id, details in students.items():
    print("----------")
    print("student id :",student_id)
    print("student name :", details["name"])
    print("student marks :", details["marks"])
print("----------")        
#count how many stud marks above 80
count = 0

for student_id, details in students.items():
   if details["marks"] > 80:
       count += 1    
print("Students marks above 80 are :",count)
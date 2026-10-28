students = {
    "S101": {"name": "Rahul", "marks": 85},
    "S102": {"name": "Priya", "marks": 92},
    "S103": {"name": "Amit", "marks": 67},
    "S104": {"name": "Sneha", "marks": 92},
}

topper_marks = 0

for student in students.values():
    if student["marks"] > topper_marks:
        topper_marks = student["marks"]

for student in students.values():
 if student["marks"] == topper_marks:
     print("Class Topper is", student["name"], "and obtained marks are", student["marks"])
   


    




students = {
    "S101": {"name": "Rahul", "marks": 85},
    "S102": {"name": "Priya", "marks": 92},
    "S103": {"name": "Amit", "marks": 67},
    "S104": {"name": "Sneha", "marks": 78},
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
print("----------")    

# find topper and print class topper name and marks

topper_marks = 0
topper_name = ""

for stud_id, details in students.items():
    #print(details["marks"])

    if details["marks"] > topper_marks:
        topper_marks = details["marks"] 
        topper_name = details["name"]

print("The topper name is :", topper_name)
print("The topper marks is :", topper_marks)

students["S103"]["marks"] = 75


for student_id, details in students.items():
    print("----------")
    print("student id :",student_id)
    print("student name :", details["name"])
    print("student marks :", details["marks"])
print("----------")

# calculate the average of all students
# avg = marks1 + marks2 + .... marksn/ stud1+stud2....studn

total_marks = 0
total_students = 0

for student_id, details in students.items():
    #print("student marks :", details["marks"])
    total_marks += details["marks"]
    total_students += 1
average = total_marks / total_students
print("Average of class is ",average)



                 




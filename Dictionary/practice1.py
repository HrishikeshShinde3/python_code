# student data is input

students = {
    "Rahul": 85,
    "Amit": 72,
    "Priya": 91
}

students.update({"Amit" : 80})
print(students)

employees = {
    "E101": {"name": "Rahul", "salary": 35000},
    "E102": {"name": "Priya", "salary": 45000},
    "E103": {"name": "Amit", "salary": 30000}
}

if "E102" in employees:
    print("Employee found")

if "E104" in employees:
    print("Employee found")
else:
    print("Employee not found")
print()

for value in employees.values():
    #print(value)
    for value1 in value.values():
        #print(value1)
        if value1 == 45000:
            print("Yes given salary is exist in data :", value1)
print()
for employee in employees:
    if employee == "E103":
        employees.update({"E103":{"name": "Amit", "salary": 35000}}) 

print(employees)
    



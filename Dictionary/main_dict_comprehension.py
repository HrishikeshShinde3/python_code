# Dictionary Comprehension
  # is a method to create a new dictionary
  # using a single expression with a loops
  # and conditions

numbers = [1,2,3,4,5]
squares = {}

for num in numbers:
    squares[num] = num * num
#print(squares)

employees = {
    "E101": {"name": "Rahul", "salary": 35000},
    "E102": {"name": "Priya", "salary": 55000},
    "E103": {"name": "Amit", "salary": 28000},
    "E104": {"name": "Sneha", "salary": 65000},
    "E105": {"name": "Neha", "salary": 45000}
}

#high salary employees

high_salary = {
    emp_id: details["salary"]
    for emp_id, details in employees.items()
    if details["salary"] >= 45000
}
print(high_salary)

# print emp ids and names

employee_details = {
    emp_id: details["name"]
    for emp_id, details in employees.items()
}
print(employee_details)





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
    "E105": {"name": "Neha", "salary": 45000},
    "E106": {"name": "Sahil", "salary": 25000},
    "E107": {"name": "Ram", "salary": 78000},
    "E108": {"name": "Alica", "salary": 33000},
    "E109": {"name": "Manish", "salary": 29000},
    "E110": {"name": "Suma", "salary": 31000}
}

# find the highest and lowest salaried employees.

L = []

for key, value in employees.items():
    L.append(value["salary"])

sorted_salary = sorted(L)

for salary in sorted_salary:
    if salary == sorted_salary[0]:
        print("Minimum salaried employee", salary)
    if salary == sorted_salary[-1]:
        print("Maximum salaried employee", salary)











    

   










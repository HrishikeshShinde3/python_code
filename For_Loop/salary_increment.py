
# []  --> List
# {}  --> Dictionary

employees = [
    {"name":"sahil","salary":25000},
    {"name":"rahul","salary":30000},
    {"name":"yash","salary":20000}

]

#print(employees)

increment_want_to_give = int(input("Enter how % do you want to give increment"))

for employee in employees:
    new_salary = employee["salary"]*increment_want_to_give
    print("Incremented salary of" ,employee["name"], "is :",new_salary)
   

# fruit = ['apple','mango']
# for fruits in fruit:
#   print("fruit name is", fruits) 

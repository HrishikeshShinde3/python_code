
# find the average of salary

my_data = {
    101: {"emp_name": "David", "salary": 25000},
    102: {"emp_name": "Prince", "salary": 35000},
    103: {"emp_name": "Glenn", "salary": 30000},
    104: {"emp_name": "Glenn", "salary": 50000},
    105: {"emp_name": "Glenn", "salary": 100000}
}

salary_sum = 0
total_employees = 0

for key, value in my_data.items():
    salary_sum += value["salary"]
    total_employees += 1
print("Average is :",salary_sum/total_employees)
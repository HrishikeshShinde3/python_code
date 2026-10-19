from math import floor


salaries = [25000, 42000, 18000, 55000, 32000, 75000, 29000]

# 1. Find Total salary -> inbuilt function

for salary in salaries:
    total = sum(salaries)
print("Total salary distribution required is : ",total)


# 1. Find Total salary -> using simple loginc

salary_sum = 0

for salary in salaries:
    salary_sum = salary_sum + salary
print("Total salary distribution required is : ",salary_sum)


# find Average salary 

salary_sum = 0 
employee_count = 0 

for salary in salaries:
    salary_sum = salary_sum + salary
    employee_count = employee_count + 1

print("Total employees are :",employee_count)

Avg_salary = floor((salary_sum / employee_count) )
print("Average salary is : ",Avg_salary)

# earning more than average salary


for salary in salaries:
 if salary > Avg_salary:
    print("employee earning more than avg salary",salary)

# earning more than 30000

for salary in salaries:
    if salary > 30000:
        print("Salary is greater than ",salary)

        




    
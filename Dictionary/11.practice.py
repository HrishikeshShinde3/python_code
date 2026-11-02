employees = [
    {'name': 'Amit', 'salary': 50000},
    {'name': 'Riya', 'salary': 70000},
    {'name': 'Sam', 'salary': 60000}
]

for i in range(len(employees)):
    for j in range(i + 1, len(employees)):
        if employees[i]['salary'] < employees[j]['salary']:
            employees[i], employees[j] = employees[j], employees[i]

print(employees)
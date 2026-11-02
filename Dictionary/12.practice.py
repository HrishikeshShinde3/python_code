employees = [
    {'name': 'Hrishi', 'salary': 60000},
    {'name': 'Amit', 'salary': 60000},
    {'name': 'Aman', 'salary': 60000},
    {'name': 'Abhay', 'salary': 60000},
    {'name': 'Sam', 'salary': 70000}
]


for i in range(len(employees)):
    for j in range(i + 1, len(employees)):
        if employees[i]['salary'] < employees[j]['salary'] or (
            employees[i]['salary'] == employees[j]['salary']
            and employees[i]['name'] > employees[j]['name']
        ):
            employees[i], employees[j] = employees[j], employees[i]

print(employees)
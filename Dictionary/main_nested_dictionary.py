n = int(input("Enter number of students: "))

students = {}

for i in range(n):
    name = input("Enter student name: ")
    marks = input("Enter student marks separated by spaces: ")

    marks = list(map(int, marks.split()))
    students[name] = marks

search_name = input("Which student's average do you want? ")

marks = students[search_name]

average = sum(marks) / len(marks)

print(f"{average:.2f}")
# create a tuple which takes mixed values as input

my_data = (1, "Alica", "Capsey", 34, 42, 22, 53 )
print(my_data)
print(type(my_data))

for index, values in enumerate(my_data):
    print(index, "=>>", values)

print(my_data[3:])
sum = 0
for data, values in enumerate(my_data):
     if data > 2:
          sum = sum + values
print("The total score is :",sum)






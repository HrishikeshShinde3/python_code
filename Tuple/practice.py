# use of "not in"

dummy = [1,2,3,2,5,6,7,5]
unique_value = []
for index, value in enumerate(dummy):
    if value not in unique_value:
        unique_value.append(value)
print(unique_value)

data = ["A","A","a","B","b","C","c","D"]
unique_data = []
for index, value in enumerate(data):
    #print(index, value)
    if value not in unique_data:
        unique_data.append(value)
print(unique_data)




    
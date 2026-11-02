
data = [6, 4, 2, 8, 3, 9]
print("Using inbuilt: ",max(data))

max_num = 0

for num in data:
    if num > max_num:
        max_num = num
print("Using loop: ",max_num)
        



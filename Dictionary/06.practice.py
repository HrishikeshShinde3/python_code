# input_list = [1, 1, 2, 3, 3, 5, 6, 7, 3, 7]
#output_data = [1, 2, 3, 5, 6, 7]

my_data = [1, 1, 2, 3, 3, 5, 6, 7, 3, 7]

output = []

for num in my_data:
    if num not in output:
        output.append(num)
print(output)



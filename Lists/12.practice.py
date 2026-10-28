# Input = [9, 23, 24, 23, 24, 21, 17, 3, 18, 2]

# Output = [9, 23, 24, 23, 24] [21, 17, 3, 18, 2]

# split the string and then add same indexes in output list

input = [9, 23, 24, 23, 24, 21, 17, 3, 18, 2]

split = len(input)/2

split_array_1 = []
split_array_2 = []

sum_of_both_array = []

for index, value in enumerate(input):
    
    if index < split:
        split_array_1.append(value)
    else:
        split_array_2.append(value)

for index1, num1 in enumerate(split_array_1):

    for index2, num2 in enumerate(split_array_2):

        if index1 == index2:
            sum = num1 + num2
            sum_of_both_array.append(sum)  

print(sum_of_both_array)
    




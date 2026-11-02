# sort without built in

L = [ 7, 4, 8, 3, 11, 2, 1, -6] 

# find max and min number

max_num = 0 
min_num = 0
for num in L:
    if max_num < num :
        max_num = num
    else:
        min_num = num
print("Small Num is:",min_num)
print("Big Num is:",max_num)


# find the missing numbers in array

missing_numbers = []
sorted_list = []   

for num in range(min_num, max_num):
    if num not in L:
        missing_numbers.append(num)
    else:
        sorted_list.append(num)
print("Missing numbers are:",missing_numbers)
print("Unique Sorted list is:",sorted_list)  # only we will get unique sort
print("Second largest number is:",sorted_list[-2])




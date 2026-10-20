
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]

for num in list2:
    #print(num)
    if num not in list1:
        #print(num)
        list1.append(num)
print(list1)


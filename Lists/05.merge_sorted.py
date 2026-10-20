# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

list1 = [1,2,4]
list2 = [1,3,4]

for num in list2:
    #print(num)
    if num in list1 or num not in list1:
        list1.append(num)
#print(list1)
list1.sort()
print(list1)

L = [ [1,2,[3,4,5],6,7], 8]

L1 = []

for nums in L:
    if type(nums) == int:
        L1.append(nums)
    elif type(nums) == list:
        for num in nums:
            if type(num) == int:
                L1.append(num)
            elif type(num) == list:               
                for n in num:
                    L1.append(n)   
print("Flattened the list :",L1)

    
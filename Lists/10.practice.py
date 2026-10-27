# find missing number from the lists

# num=[1,0,3,4] = [0,1,2,3,4]
# op=2


num1=[9,6,4,2,3,5,7,0,1]
# op=8




length_of_array = 0 

for i in num1:
    length_of_array = length_of_array + 1

for num in range (0, length_of_array):
        if num not in num1:
               print("Completed :",num)
    
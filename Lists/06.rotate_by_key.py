# l = [1,2,3,4]
# no._of_rotations = 2
# rotated_list = [3,4,1,2]

input_list = [1,2,3,4]
key_index = 2
rotated_list = []

length_of_input_list = len(input_list)

if key_index not in range(1,length_of_input_list):
   print("Please enter valid key for rotation")
else:
    for index, number in enumerate(input_list):
        #print(index, number)
        if index >= key_index:
            rotated_list.append(number)

    for index, number in enumerate(input_list):
        if index < key_index:
            rotated_list.append(number)
    
        
print(rotated_list)



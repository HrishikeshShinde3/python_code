#Q16. Find the longest sequence of consecutive 1s

# Given a list containing only zeros and ones, find the maximum consecutive run of ones.

# Example: [1, 1, 0, 1, 1, 1, 0, 1] → 3

data = [1, 1, 0, 0,-1,-4,-5,1,2,3,4,5,1,1,1,0, 0, 1, 5, 1,1,4,1,1,1,1,1, 0, 1]

new_list = []
number = []

for num in data:
    if num != 0:
        number.append(num)
    else:
        if number:
            new_list.append(number)
            number = []

if number:
    new_list.append(number)
    
print("-------------------")
print("Longest sequence is :",max(new_list, key=len))
longest_sequence = len(max(new_list, key=len))
print("-------------------")
print("Consecutive non zero numbers",longest_sequence, "times.")
print("-------------------")
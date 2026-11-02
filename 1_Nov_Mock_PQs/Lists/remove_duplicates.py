
L = [ 2, 2, 1, 0, 0, 3, 4, 5, 5]
removed_the_duplicates = []
removed_duplicates = []
for num in L:
    if num not in removed_the_duplicates:
        removed_the_duplicates.append(num)
    else:
        removed_duplicates.append(num)
print("Duplicates removed :",removed_the_duplicates)
print("Removed duplicates numbers are :",removed_duplicates)
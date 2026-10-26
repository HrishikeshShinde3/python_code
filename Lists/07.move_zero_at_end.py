# nums=[1,0,2,4,3,0,0,3,5,1]  move all zero at end preserving the order.
# o/p = nums=[1,2,4,3,3,5,1,0,0,0]

name_data = ["Glenn", "David", "Steven", "Alex", "Jaison", "Chris"]

asc_all_alphabet_data = []  # to store all A to Z
first_alphabets = []  # to store first chr of each list string

for i in range(ord('A'), ord('Z') + 1):
     asc_all_alphabet_data.append(chr(i))
print("All char :",asc_all_alphabet_data)   


for word in name_data:
     #print(word[0]) 
     first_alphabets.append(word[0])   
print("First char :",first_alphabets)

for character in asc_all_alphabet_data:
     #print(character)
     if character in first_alphabets:
          print(character, "is present in the list")
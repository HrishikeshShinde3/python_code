name_data = ["Glenn", "David", "Steven", "Alex", "Jaison", "Chris"]
final_data = []
asc_all_alphabet_data = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
     "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
     "U", "V", "W", "X", "Y", "Z"]

for alphabet in asc_all_alphabet_data:
     #print(alphabet)
     for word in name_data:
          if alphabet == word[0]:
               final_data.append(word)
print("Output is :", final_data)

# reverse the given number

# input= 544656
# output= 656445

num = "544656"
reverse = ""

for i in range(1, len(num) + 1):
    reverse = reverse + num[-i]
print(reverse)



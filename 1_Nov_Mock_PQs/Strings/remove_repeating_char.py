# remove non repeating characters from string
# -> HISH

A = "HRISHIKESH"

Output = []

for index, chr in enumerate(A):

 starting_chr = A[index]
 count = 0

 for index, chr in enumerate(A):
    if starting_chr == chr:
     #print(index, chr)
     count += 1
 #print(starting_chr, "->",count)

 if count == 1 :
   print("Unique characters are :",starting_chr, count)
 else:
  print("Repeated characters arr :",starting_chr, count)
index += 1



print(Output)





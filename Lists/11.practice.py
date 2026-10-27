
a=[1,2,3,4]
b=[5,4,3,0]

output_list = []


key = 7

# means (2,5) = 7

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] + b[j] == 7:
            output_list.append([a[i], b[j]])
            
#print(output_list)           
# find duplicate and count the frequency

name = "programming"

output = []
output_occurence = []

for chr in name:
    output.append(chr)
print(output)




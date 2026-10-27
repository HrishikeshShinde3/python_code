num1=[ 1, 1,1.2,4,6,7]
num2 =[1,2,3,6,7,8,9,10]

round_off_list1 = []
round_off_list2 = []

output_list = []
# op:- [1,2,3,4,6,7,8,9,10]

for n in num1:
    round_off_list1.append(round(n))
print(round_off_list1)

for n in num2:
    round_off_list2.append(round(n))
print(round_off_list2)

for n in round_off_list2:
        output_list.append(n)
print(output_list)

for n in round_off_list1:
        if n not in output_list:
         output_list.append(n)
print(output_list)
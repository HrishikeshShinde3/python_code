
L1 = (60,50,40,30,20,10)

number = []

for num in L1:
    if num not in number:
        number.append(num)
a = sorted(number)
print("The second highest is :",a[-2])
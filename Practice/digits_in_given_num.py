num = int(input("Enter the number :"))

total = 0

while num > 0 :

    num = num // 10
    total = total + 1

print(total,"digits are in given number.")
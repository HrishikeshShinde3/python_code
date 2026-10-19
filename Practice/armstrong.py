# check the given num is armstrong or not 

num = int(input("Enter the number :"))

armstrong = num

total = 0

while num > 0 :

    digit = num % 10
    total = total + digit **3
    num =  num // 10

if armstrong == total:
    print("Given number is Armstrong Number")
else:
    print("Given number is Not ArmStrong Number")

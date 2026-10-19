num = int(input("Enter the number :"))

largest = 0

while num > 0:

    digit = num % 10 # 5
    if digit > largest :
        largest = digit
    num = num // 10
    
print(largest)


"""

Smallest digit from number

smallest = 9

while num > 0 :

    digit = num % 10 
    num = num // 10 
    if digit < smallest
       smallest = digit

"""
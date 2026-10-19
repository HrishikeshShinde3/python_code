"""
Input = Num = 123
output = Sum = 1+2+3 = 6

"""

num = int(input("Enter the number :"))

Sum = 0

while num > 0 :

    last_digit  = num % 10
    Sum = Sum + last_digit
    num = num // 10

print(Sum)


"""
num = int(input("Enter the number :"))

Product = 1

while num > 0 :

    last_digit  = num % 10
    Product = Product * last_digit
    num = num // 10

print(Product)

"""
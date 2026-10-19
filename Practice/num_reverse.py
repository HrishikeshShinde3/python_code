

"""
print(1234 % 10) #4
print(123 % 10)  #3
print(12 % 10)   #2
print(1 % 10)    #1

print(1234 / 10) #123.4
print(123 / 10)  #12.3
print(12 / 10)   #1.2
print(1 / 10)    #0

print(1234 // 10) #123 // < Divides two nums and return round off number
print(123 // 10)  #12  // it is known as floor division
print(12 // 10)   #1
print(1 // 10)    #0
"""

num = int(input("Enter the number :"))

reverse = 0

while num > 0:

    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed num is :", reverse)



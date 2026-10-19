"""
input = num = 121
output = 121 = num is palindrome

"""

num = int(input("Enter the number :"))

original = num
reverse_num = 0

while num > 0 :
    digit = num % 10
    reverse_num =  reverse_num * 10 + digit
    num = num // 10
print(reverse_num)

if original == reverse_num :
    print("Num is Palindrome")
else:
    print("Num is Not Palindrome")
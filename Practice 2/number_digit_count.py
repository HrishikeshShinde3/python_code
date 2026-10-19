"""
Input = num = 1234
Output = digit = 4

"""
print(1 // 10)

num = int(input("Enter the Number : "))

digit_count = 0

while num > 0 :

    num = num // 10
    digit_count = digit_count + 1

print(digit_count)
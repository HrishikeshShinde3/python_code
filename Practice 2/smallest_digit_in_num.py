num = int(input("Enter the number :"))

smallest = 9

while num > 0 :
    digit = num % 10 
    if digit < smallest:
        smallest = digit
    num = num // 10
print(smallest)
num = int(input("Enter the number :"))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if(num % i == 0):
            is_prime = False
            break
if is_prime:
    print("Given number is prime")
else:
    print("Given number is not prime")



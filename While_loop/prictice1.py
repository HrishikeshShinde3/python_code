# print 1 to 5 numbers using while loop

num = 1

while num <= 5:
    print(num)
    num = num + 1


# print 5 to 1 

num = 5

while num <= 5 and num > 0:
    print(num)
    num = num - 1


#print even number from in 1 to 10

num = 1 

while num <= 10:
    if num % 2 == 0:
     print("Even number is :",num)
    else:
     print("Odd number is :",num)
       
    num = num + 1

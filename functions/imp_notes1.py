# functions is reusable block of code that
      # perform a perticular set of tasks

#write a function to add two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def add_numbers(num1,num2): # def is to define a function
    print(num1+num2)
add_numbers(a,b)            # add_numbers is func name
                            # () contain parameters
                            # calling the function and executes its body.


# in above example num1 and num2 are parameters
# & a and b are the arguments
print()
print("----return VS print()----") 

# print() displays a value, but it does not
# send that value back to the caller
# without and explicit return, python returns none


#using return

def add(a,b):
    return a + b

result = add(10, 20)
print("result :",result)

# return() sends the result back, allwed to it 
# in variable or use it in another calculation

# positional and keyword arguments

# 1. Positional arguments

    




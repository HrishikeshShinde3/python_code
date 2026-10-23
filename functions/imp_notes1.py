# functions is reusable block of code that
      # perform a perticular set of tasks

#write a function to add two numbers

a = 3
b = 4

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

def person_details(name, age):
    print(f"Hello! My name is {name} and my age is {age}")


person_details(22, "Hrishi")
# output is = Hello! My name is 22 and my age is Hrishi
# py assign the values by position not by  the names

# 2. Keyword arguments

def my_details(name, age):
    print(f"My name is {name}. My age is {age}")

my_details(age = 26, name = "Hrishi")


# Default arguments

def employee(name, city = "pune", salary = 30000):
    print(name)
    print(city)
    print(salary)

employee("Hrishikesh", "mumbai", 45000)

# parameters without defaults must come before parameter with defaults
# mean argument having first priority if any argument is missing
# then default parameters comes in the role







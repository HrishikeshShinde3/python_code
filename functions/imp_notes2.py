# Arguments = *args
   # *args can use if we dont know how many
    # arguments a function will receive.

def add_numbers(*args):
    total = 0
    for num in args:
        total += num

    return total

print(add_numbers(10, 20, 30))


# arguments with normal parameters

def student_marks (name,*marks):
    print("student", name)
    print("marks", marks)

student_marks("rahul", 80,85,90)

print()
# **kwargs (KeyWordArguments)

def students_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
    print(kwargs)
students_details(name = "steven", age = 39, city = "sydney")
print()

# **kwargs to print product details

def product_details(**kwargs):
    
    for key, value in kwargs.items():
        print(key, ":",value)
    total_price = kwargs["price"] * kwargs["quantity"]
    print("total sale is ",total_price)
product_details(name="laptop", price=50000, quantity=2)


# Dictionary methods

employee = {
    "name" : "Rahul",
    "age" : 25,
    "role" : "Python Developer",
    "salary" : 35000
}

# data.key
#print(employee.keys())

# data.values
#print(employee.values())

# data.item
#print(employee.items())


# Dictionary methods

# 1. keys(), values() and items()
# print(employee.keys())
# print(employee.values())
# print(employee.items())

print()

# 2. Dict methods with loops
print("---- Dict methods with loops----")

 #for key, value in employee.items():
    #print(key, ":", value)

# write a code to   
  # print each city and its sale
  # find total sale
  # find and print the city with highest sales.

sales = {
    "Pune": 45000,
    "Mumbai": 62000,
    "Nashik": 38000,
    "Nagpur": 55000,
    "Thane": 30000
}

total_sale = 0

max_sale = max(sales.values())
print("Max sale is :",max_sale)
# print the city name in which sale is highest

for key, value in sales.items():
    total_sale += value
    if max_sale == value:
        print("Max sale happened in ",key)

# print total sale happened
print("Total sale happened :",total_sale)


# Dictionary methods update(), pop(), popitem() and clear()

# 1. Update

sales.update({
    "kalyan" : 65000,
    "New Mumbai" : 70000,
    "Thane" : 59000
})
print(sales)






























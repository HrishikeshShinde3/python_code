sales = {
    "Pune": 45000,
    "Mumbai": 62000,
    "Nashik": 38000,
    "Nagpur": 55000,
    "Thane": 30000
}

# update pune to 50000
sales.update({ "Pune": 50000,})
print(sales)

# add Nanded = 42000
sales.update({"Nanded" : 42000})
print (sales)

# remove nanded and stored it in variable
last_removed = sales.pop("Nanded")
print(sales)
print()
print(last_removed)

# print total sales of all remaining cities






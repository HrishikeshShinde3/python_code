monthly_sales = (12000, 15000, 11000, 18000)
print(monthly_sales)

sales_list  = list(monthly_sales)
print("easy way", sales_list)

for i in monthly_sales:
    print(i)
    sales_list.append(i)

print(sales_list)

sales_list.insert(2,13500)
print(sales_list)

sales_list.remove(11000)
print(sales_list)

sales_list.append(20000)

print(sales_list)




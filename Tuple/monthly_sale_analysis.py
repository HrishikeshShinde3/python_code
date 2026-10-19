monthly_sales = (25000, 32000, 25000, 45000, 38000, 32000, 50000, 45000)
print("inbuilt sum :",sum(monthly_sales))
# calculate the total sales in month
print("Total sale is :",sum(monthly_sales))

# highest sale and lowest sale
print("Max sale is :",max(monthly_sales))
print("Min sale is :",min(monthly_sales))

# calculate the average sale

#avg_sale = sum(monthly_sales)/ no_of_days

print("Sales days :",len(monthly_sales))

avg_sale = sum(monthly_sales)/ len(monthly_sales)

print("Average Sale per day is :",avg_sale)

# count the occurance of 25000

print(monthly_sales.count(25000))


for each in monthly_sales:
    print(each)
                                                                                                                                                                    
# find first occurence of 45000

print("first occurence of 45000 at index:",monthly_sales.index(45000))
print("first occurence of 32000 at index:",monthly_sales.index(32000))

for value in monthly_sales:
    if value == 50000:
        print("Given sale number is existed in the data")

# create new tuple and put last four figures in it.

print(monthly_sales[-4:])  #slicing 
  
# remains unchaged
 

print(monthly_sales)




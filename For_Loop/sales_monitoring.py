#find below from given data

# Total sales
# Average sales
# Number of days where sales were above average
# Number of days where sales were below ₹10,000
# Print "TARGET ACHIEVED" for sales ₹15,000 or more 

sales = [12000, 8500, 15000, 4200, 18000, 9500, 22000, 6700, 12500]

#total sales

total_sales = 0 

for sale in sales:
    total_sales += sale 
print(total_sales)

# Average sales




         # sales happened days

total_sales_day = 0

for sale in sales:
    total_sales_day = total_sales_day + 1
print("Total sales happened days are :", total_sales_day)

# average sales

average_sales = 0

for sale in sales:
    average_sales = total_sales/total_sales_day
print(average_sales)

# Number of days where sales were above average

sale_above_average_day = 0

for sale in sales:
    if sale > average_sales:
       sale_above_average_day = sale_above_average_day + 1
print("Days where sales were above average :", sale_above_average_day)

# Number of days where sales were below ₹10,000

below_sale_10k = 0 

for sale in sales:
    if sale < 10000:
        below_sale_10k = below_sale_10k + 1
print("No of day were sale is below 10,000 : ", below_sale_10k)


for sale in sales:
    if sale > 15000:
        print("Sales done of ",sale,"target achieved !")






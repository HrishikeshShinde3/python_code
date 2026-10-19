
sales_data = (
    ("Pune", 45000),
    ("Mumbai", 62000),
    ("Nashik", 38000),
    ("Pune", 51000),
    ("Mumbai", 55000)
)

# count how many records belongs to pune

count=0
city='Pune'
for index, value in enumerate(sales_data):
    if city in value:
        count=count+1
        print("Record found at index:",index)
        print("Record is :",value)    
print(count)


print("----------Calculate the total sales-------------")

total_mumbai_sales= 0 
city ="Mumbai"
for mumbai_sales in sales_data:
    if city in mumbai_sales:
      total_mumbai_sales += mumbai_sales[1]
print("Total sale in mumbai is :",total_mumbai_sales)
print()

print("-------Find the highest individual sale--------")

max_sale = 0
max_record = None
for highest_sale in sales_data:
    if max_sale < highest_sale[1]:
        max_sale = highest_sale[1]
        max_record = highest_sale
print(max_record)

print()

print("----list containing only the city names----")

city_name =[]

for index, value in (sales_data):
    city_name.append(index)
print(city_name)

sales_numbers = []

for index, value in sales_data:
    sales_numbers.append(value)
print(sales_numbers)

# remove duplicates cities from the list and create a new list with unique cities


unique_cities = []

for city in city_name:
    if city not in unique_cities:
        unique_cities.append(city)
print()        
print("Unique cities are",unique_cities)
    
print(sales_data)

# calculate the total sum for the each city

pune_sales = 0
mumbai_sales = 0
nashik_sales = 0

for index, values in sales_data:
    if index == "Pune":
        pune_sales += values
    if index == "Mumbai":
        mumbai_sales += values
    if index == "Nashik":
        nashik_sales += values
print("Total sale for Pune :", pune_sales)
print("Total sale for Mumbai :", mumbai_sales)
print("Total sale for Nashik :", nashik_sales)
print()
print()

# calculate the total sum for the each city

unique_city = []

for index, values in sales_data:
          if index not in unique_city:
           unique_city.append(index)
print(unique_city)


# calculate the total sum for the each city

    # iterate through the given data and add indexing in it

    # calculate the total sum

total_sale = 0 

for index, values in sales_data:
  total_sale = total_sale + values
print("Total sale is :", total_sale)

print()

# calculate the total sum for the each city

   # 1. iterste through unique cities

for city in unique_cities:

   #2. Initializes a total of 0 for that city.
  
    total_sale = 0

    #3. Iterate throgh sales dat

    for index, value in sales_data:
        if index == city:
         total_sale += value
    print("Total sale :", total_sale)







 





# Iterates through sales_data.
# Adds the sale amount when the record's city matches the current city.

# Prints that city's total.









        
        


    
    




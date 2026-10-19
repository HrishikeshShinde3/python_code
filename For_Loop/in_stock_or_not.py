# "Out of Stock" when stock is 0
# "Low Stock" when stock is between 1 and 5
# "In Stock" when stock is greater than 5

stock = [10,9,8,7,6,5,4,3,2,1,0]
 
for remaining_stock in stock:
      if remaining_stock == 0:
         print("out of stock")
      elif remaining_stock > 0 and remaining_stock <= 5:
         print("Low stock")
      else:
         print("In stock")
      

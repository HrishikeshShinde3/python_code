# calculate_sales

def calculate_sales(*sales):
    #print(*sales)
    total = 0
    for each_sale in sales:
        #print(each_sale)
        total = total + each_sale

    max_sale = 0

    for each_sale in sales:
        if each_sale > max_sale:
            max_sale = each_sale
    print("total sales :", total)
    print("highest sale :", max_sale)           
    return total, max_sale
    
total_sale = calculate_sales(23,77,50,100)
print("total sale and max sale is :",total_sale)
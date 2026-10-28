my_data = (("Dev", [55, 65, 75]), ("Maya", [60, 60, 60]),
            ("Rishi", [67, 65, 65]), ("Om", [90, 80, 70]))


for data in my_data:
        if sum(data[1])/3  >= 65:
         print(data[0], "is pass")
        else:
         print(data[0], "is fail")
        
        
        
        

        
row1= ['1','2','3']
row2= ['4','5','6']
row3= ['7','8','9']

num = str(input("Enter the number to hide :"))

if num in row1:
    print("row1")
    for index, value in enumerate(row2):
            
              if num == value: 
                print(index, value)
    row1.insert(index, "X")
    row1.remove(num)
              
           
elif num in row2:
    print("row2")
    for index, value in enumerate(row2):
                
                if num == value:      
                   print(index, value)
     
    row2.insert(index, "X")
    row2.remove(num)
    
             
            
else:
    print("row3")
    for index, value in enumerate(row3):
            
            if num == value:
                print(index, value)
    row3.insert(index, "X")
    row3.remove(num)
    
print(row1)
print(row2)
print(row3)







    
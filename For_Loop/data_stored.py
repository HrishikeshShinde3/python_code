import json 

data = [] 

for i in range (3): 
    first_name = input("Enter first name :"),
    last_name = input("Enter Last name :"),
    data.append(                  #append() is a list method used to add one new item at the end of a list.
        { "id": i+1, 
         "first_name": first_name, 
         "last_name": last_name }
        ) 
    
with open("loops.json","w" ) as file:  #stored all data in lopps.json file
        json.dump(data,file) 

print("Data saved successfully !")
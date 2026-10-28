# removed empty tuple without changing the sequence

list =[1,2,(1,2,3),8,9,3,(),5,0,(8,9),()]

output_list = []

for data in list:

     if isinstance(data, tuple):
    
        if data != ():
            print(data)
            output_list.append(data)
     else:
         output_list.append(data)
     
print(output_list)
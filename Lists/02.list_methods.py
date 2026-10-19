# Create one empty list to store user basket fruits

fruit_basket = []

# basket_strength = int(input("How many fruits do you want to add :"))

# for i in range(basket_strength):
#     fruit_name = input("Enter fruit name :")
#     fruit_basket.append(fruit_name)
# print("Your fruit basket is ready :",fruit_basket)

fruit_basket.extend(['Apple', 'Banana', 'Cherry', 'Mango', 'Watermelon', 'Cherry', 'Chickoo', 'Pineapple', 'Banana', 'Mango'])


fruit_basket.insert(3,'Dog')


fruit_basket.remove('Dog')


fruit_basket.pop(1)


fruit_basket.sort()


fruit_basket.reverse()



for i in range(len(fruit_basket)):
    if fruit_basket[i] == 'Banana':
        print(i)


print(fruit_basket.count('Cherry'))



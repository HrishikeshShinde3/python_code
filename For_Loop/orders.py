orders = [
    {"product":"Laptop", "price":55000},
    {"product":"TV", "price":8000},
    {"product":"Mobile", "price":2000},
    {"product":"Wasing machine", "price":25000},
    {"product":"Mixer", "price":4500},
]

for order in orders:

    if order["price"] > 25000:
        print(order["product"], "is a high value order")

    elif order["price"] >= 10000 and order["price"] <= 25000:
        print(order["product"], "is a mid value order")

    else:
        print(order["product"], "is a low value order")
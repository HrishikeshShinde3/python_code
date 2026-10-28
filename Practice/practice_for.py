d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 25}

merged={}

for key, value in d1.items():
    if key not in merged:
        merged[key] = value
for key, value in d2.items():
    if key not in merged:
        merged[key] = value
    else:
        merged[key]+=value

print(merged)










print("------------")

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 25, 'a':10}

d1['a'] = d1['a'] + d2['a'] 
d1['b'] += d2['b']
d1['c'] += d2['c']
d1['d'] = d2['d']

print(d1)
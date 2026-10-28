s =(("Dev", [55, 65, 75]),
    ("Maya", [60, 60, 60]), 
    ("Om", [90, 80, 70]))  

for i in range(len(s)):
    sum1 = sum(s[i][1])
    avg = sum1// len(s[1][1])
    # print(avg)
    if avg >= 65:
        print(s[i])
    
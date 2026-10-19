
#* Input strings: ['ab', 'ab', 'abc']
#* Comparison strings: ['ab', 'abc', 'bc']
#* Output: [2, 1, 0] 
#* (Because 'ab' appears twice, 'abc' 
# appears once, and 'bc' appears zero times).

input_string = ['ab', 'ab', 'abc']
comparison_string = ['ab', 'abc', 'bc']

ab = 0
abc = 0
bc = 0

for text in input_string:
    if text in comparison_string:
        if text == "ab":
            ab += 1
        if text == "abc":
                    abc += 1
        if text == "bc":
                    bc += 1
print(ab)
print(abc)
print(bc)

output_list = [ab, abc, bc]
print(output_list)


        
        




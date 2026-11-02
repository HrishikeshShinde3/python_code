# Find the longest common prefix of a list of words.
# Input : words = ['flower', 'flow', 'flight']
# Output: "fl"

L = ['flower', 'flow', 'float','floght','flour']
string = ""
print(L[0][0])
for index, value in enumerate(L):
      
    if all (value[index] == L[index][index] for value in L):
       #all() checks whether every word has the same first character.
       string += L[index][index] 
    
#print(string)

    
        
     
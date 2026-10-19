
# Create a string variable called `my_string` and assign it the value "Hello, World!".

my_string = "Hello World"

print("The string is :",my_string)  

count = 0

# calculating the length of the string

for i in my_string:
    count = count + 1
print("Total string length is :",count)


# indexing of string

s = "Hello World"

print(s[8])

# string slicing

print(s[0:7])
print(s[6:10])

print(s[:6]) # ommiting the front
print(s[6:]) # ommiting the back
print(s[:])  #copy entire string

# step slicing syntax -> string[start:end:step]

print(s[0:11:2]) # op > HloWrd

num = '123456789'
print(num[0:10:2])
length = len(num)
print("Length of string :",length)
print(num[::-1])

# dynamic slicing

User_string = input("Enter your string :")

start = int(input("Enter the starting index :"))
end = int(input("Enter the last index :"))

print(User_string[start:end])


text = input("Enter your mail id :")

index = text.index('@')

print(index)

print("Domain name is :",text[index+1:])

string = "Hello World"

print(string[0:5])     # Hello
print(string[:5])      # Hello
print(string[6:])      # World
print(string[-5:])     # World
print(string[::2])     # HloWrd
print(string[::-1])    # dlroW olleH
print(string[1:-1])    # ello Worl










 

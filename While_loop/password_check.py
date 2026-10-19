# password check system

# Correct password is "admin123"
# Ask the user to enter the password.
# If the password is correct → print "Login successful" and stop the loop.
# If incorrect → print "Invalid password".
# After 3 wrong attempts → print "Account locked".

password = "admin123"

entered_password = input("Enter the password :")

attempts = 0

while password != entered_password:
    print("Invalid password")
    entered_password = input("Enter the password :")
    attempts = attempts + 1
    print("Attempts remianing: ", 3 - attempts)
    if attempts >= 3:
        print("Account locked")
        break
else:
     print("Login successful")
  
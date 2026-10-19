# Employee attendance tracking program

# 1. Ask the employee how many hours they worked each day.

working_hours = int(input("Enter the working hours :"))

while working_hours != 0 :
    if working_hours >= 8:
        print("You have worked full hours today.")
    elif working_hours < 8 and working_hours > 0:
        print("You have worked part-time hours today.")
    else:
        print("Invalid input. Please enter a positive number of hours.")

    working_hours = int(input("Enter the working hours :"))

# password_manager.py

import json
import os

FILE_NAME = "passwords.json"


# Load saved passwords
def load_passwords():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


# Save passwords
def save_passwords(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# Add new password
def add_password():
    website = input("Enter Website Name: ")
    username = input("Enter Username/Email: ")
    password = input("Enter Password: ")

    data = load_passwords()

    data[website] = {
        "username": username,
        "password": password
    }

    save_passwords(data)

    print("\n✅ Password Saved Successfully!")


# View saved password
def view_password():
    website = input("Enter Website Name to Search: ")

    data = load_passwords()

    if website in data:
        print("\n===== Account Details =====")
        print("Website :", website)
        print("Username:", data[website]["username"])
        print("Password:", data[website]["password"])
    else:
        print("\n❌ No Data Found!")


# Main file
while True:
    print("\n")
    print("1. Add Password")
    print("2. View Password")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_password()

    elif choice == "3":
        print("\n👋 Exiting Password Manager...")
        break

    else:
        print("\n❌ Invalid Choice! Try Again.")
        
import os
import json

FILE_NAME = "vault.json"

# Load existing passwords
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save passwords to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add a new entry
def add_password():
    site = input("Enter the website name: ")
    username = input("Enter your username/email: ")
    password = input("Enter your password: ")
    data = load_data()
    data[site] = {"username": username, "password": password}
    save_data(data)
    print("✅ Password saved!")

# View stored entries
def view_passwords():
    data = load_data()
    if not data:
        print("🔒 No passwords stored yet.")
        return
    print("\nStored passwords:")
    for site, creds in data.items():
        print(f"🌐 {site} - 👤 {creds['username']} | 🔑 {creds['password']}")

# Menu
def menu():
    while True:
        print("\n=== SecureVault Menu ===")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("👋 Exiting SecureVault. Stay secure!")
            break
        else:
            print("❌ Invalid option. Try again.")

menu()

import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

# Load saved data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add a new transaction
def add_transaction():
    t_type = input("Type (Income/Expense): ").strip().lower()
    if t_type not in ["income", "expense"]:
        print("❌ Invalid type. Try again.")
        return

    amount = float(input("Amount: ₹"))
    category = input("Category (e.g., Food, Salary, Bills): ")
    note = input("Note (optional): ")

    entry = {
        "type": t_type,
        "amount": amount,
        "category": category,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data = load_data()
    data.append(entry)
    save_data(data)
    print("✅ Transaction saved!")

# View all transactions
def view_transactions():
    data = load_data()
    if not data:
        print("📭 No transactions yet.")
        return

    for entry in data:
        print(f"[{entry['date']}] {entry['type'].title()} | ₹{entry['amount']} | {entry['category']} | {entry['note']}")

# View summary
def view_summary():
    data = load_data()
    total_income = sum(entry['amount'] for entry in data if entry['type'] == 'income')
    total_expense = sum(entry['amount'] for entry in data if entry['type'] == 'expense')
    balance = total_income - total_expense

    print("\n=== Summary ===")
    print(f"💰 Total Income: ₹{total_income}")
    print(f"💸 Total Expenses: ₹{total_expense}")
    print(f"📊 Balance: ₹{balance}")

# Menu
def menu():
    while True:
        print("\n=== Daily Expense Tracker ===")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("👋 Exiting. Stay smart with your money!")
            break
        else:
            print("❌ Invalid option. Try again.")

# Run the menu
menu()


# ===========================
# EXPENSE TRACKER PROJECT
# By: Ismail Shafi
# ===========================

def add_expense():
    name = input("What did you spend on? ")
    amount = input("How much? ₹")
    
    with open("expenses.txt", "a", encoding="utf-8") as f:
        f.write(f"{name}: ₹{amount}\n")
    
    print("✅ Saved successfully!\n")


def view_expenses():
    print("\n📋 Your Expenses:")
    print("----------------")
    
    try:
        with open("expenses.txt", "r",encoding="utf-8") as f:
            content = f.read()
            if content == "":
                print("No expenses yet!")
            else:
                print(content)
    except FileNotFoundError:
        print("No expenses file found yet!")


def total_expenses():
    total = 0
    
    try:
        with open("expenses.txt", "r", encoding="utf-8") as f:
            for line in f:
                amount = line.split("₹")[1]
                total += float(amount.strip())
        
        print(f"\n💰 Total Spent: ₹{total}")
    
    except FileNotFoundError:
        print("No expenses yet!")


def clear_expenses():
    with open("expenses.txt", "w", encoding="utf-8") as f:
        f.write("")
    print("🗑️ All expenses cleared!\n")


# Main Menu
while True:
    print("====== EXPENSE TRACKER ======")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. See total")
    print("4. Clear all")
    print("5. Exit")
    
    choice = input("\nChoose (1-5): ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        clear_expenses()
    elif choice == "5":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice! Try again.\n")




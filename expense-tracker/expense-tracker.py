
print(" WELCOME TO EXPENSE TRACKER!")

total_expense = 0
expense_count = 0
expenses = []

def add_expense():
    global total_expense, expense_count
    
    try:
        amount = float(input("Enter expense amount: $"))
        total_expense = total_expense + amount
        expense_count = expense_count + 1
        expenses.append(amount)
        print(f"${amount:.2f} added! Total: ${total_expense:.2f}")
    except:
        print("Invalid amount!")

def view_total():
    print(f"Total: ${total_expense:.2f}")
    print(f"Items: {expense_count}")
    if expense_count > 0:
        avg = total_expense / expense_count
        print(f"Average: ${avg:.2f}")

def view_all():
    if len(expenses) == 0:
        print("No expenses")
        return
    for i, amt in enumerate(expenses, 1):
        print(f"  {i}. ${amt:.2f}")

while True:
    print("\n=== EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View Total")
    print("3. View All")
    print("4. Exit")
    
    choice = input("Enter (1-4): ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_total()
    elif choice == "3":
        view_all()
    elif choice == "4":
        print(f"Goodbye! Total spent: ${total_expense:.2f}")
        break
    else:
        print("Invalid choice!")

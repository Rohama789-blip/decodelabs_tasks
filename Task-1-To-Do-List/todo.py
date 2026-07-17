
print(" WELCOME TO MY TO-DO LIST APP!")
print("=" * 35)


my_tasks = []

def add_task():
    task = input("Type your task here: ")
    my_tasks.append(task)
    print("Task added!")

def view_tasks():
    
    if len(my_tasks) == 0:
        print(" Your list is empty! Add some tasks first.")
        return
    
    print("\n--- Your Tasks ---")
    for i in range(len(my_tasks)):
        print("  " + str(i+1) + ". " + my_tasks[i])


def add_multiple_tasks():
    num = int(input("How many tasks do you want to add? "))
    for i in range(num):
        task = input("Task " + str(i+1) + ": ")
        my_tasks.append(task)
    print("✅ " + str(num) + " tasks added successfully!")

def main():
    while True:
        
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Add Multiple Tasks")
        print("4. Exit")
        
        choice = input("Enter 1, 2, 3, or 4: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            add_multiple_tasks()
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print("s Wrong input! Try again.")

if __name__ == "__main__":
    main()

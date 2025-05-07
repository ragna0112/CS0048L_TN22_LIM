print("\nTo-Do List")

def menu():
    print("\nMenu:")
    print(" 1. Add Task")
    print(" 2. Remove Task")
    print(" 3. View Tasks")
    print(" 4. Exit")

def add_task(tasks):
    task = input(" Enter the task to add: ")
    tasks.append(task)
    print(" Task added.")

def remove_task(tasks):
    task = input(" Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(" Task removed.")
    else:
        print(" Task not found.")

def view_tasks(tasks):
    if tasks:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f" {i}. {task}")
    else:
        print("No saved tasks.")

def main():
    tasks = []
    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Thank you for using the to-do list system.")
            break
        else:
            print("Invalid choice. Choose from (1-4) pls.")

main()

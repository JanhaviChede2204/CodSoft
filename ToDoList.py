# To-Do List Application (CLI)

tasks = []

def show_menu():
    print("\nEnter your choice:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

def add_task():
    try:
        num = int(input("Enter number of tasks: "))
        for _ in range(num):
            task = input("Enter task: ")
            tasks.append({"task": task, "status": "Pending"})
        print("Tasks added successfully!")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} - {task['status']}")

def update_task():
    try:
        view_tasks()
        index = int(input("Enter task number to update: ")) - 1
        tasks[index]["task"] = input("Enter new task name: ")
        print("Task updated successfully!")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("Task number does not exist.")

def mark_completed():
    try:
        view_tasks()
        index = int(input("Enter task number to mark completed: ")) - 1
        tasks[index]["status"] = "Completed"
        print("Task marked as completed!")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("Task number does not exist.")

def delete_task():
    try:
        view_tasks()
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        print("Task deleted successfully!")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("Task number does not exist.")

try:
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Thank you for using To-Do List App!")
            break
        else:
            print("Invalid choice. Please try again.")

except KeyboardInterrupt:
    print("\nExiting To-Do List App. Goodbye!")

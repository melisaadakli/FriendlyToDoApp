
# To Do List
todos = []

def show_menu():
    print("\nTo-Do List Application")
    print("1. Add New Task")
    print("2. List Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")

def add_new_task():
    new_task = input("What's the new task you want to add? ")
    todos.append({"task": new_task, "status": "Not Done"})
    print("Great! Your new task has been added.")

def view_tasks():
    print("\nYour To-Do List:")
    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo['task']} - Status: {todo['status']}")

def update_task_status():
    task_number = int(input("Enter the task number you want to update: "))
    if 1 <= task_number <= len(todos):
        new_status = input("What's the new status for this task? (Done/Not Done): ")
        todos[task_number - 1]["status"] = new_status.capitalize()
        print("Got it! Task status updated.")
    else:
        print("Ooopss! That task number doesn't exist. Please try again.")

def delete_task():
    task_number = int(input("Enter the task number you want to delete: "))
    if 1 <= task_number <= len(todos):
        deleted_task = todos.pop(task_number - 1)
        print(f"Successfully removed '{deleted_task['task']}' from your list!")
    else:
        print("Noooo! That task number is not valid. Please try again.")

while True:
    show_menu()
    choice = input("What would you like to do? (1-5): ")

    if choice == "1":
        add_new_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task_status()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye! Have a wonderful day.")
        break
    else:
        print("Oops! That's not a valid option. Please choose a number from 1 to 5.")
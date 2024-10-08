# Simple To-Do List App
import sys

# Global list to store tasks
tasks = []

# Function to display the main menu
def show_menu():
    print("\nTo-Do List App")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    return choice

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✔" if task['completed'] else "✘"
            print(f"{idx}. {task['task']} [{status}]")

# Function to add a task
def add_task():
    task_name = input("\nEnter the new task: ")
    tasks.append({'task': task_name, 'completed': False})
    print(f"Task '{task_name}' added.")

# Function to mark a task as complete
def mark_task_complete():
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop to run the app
def run_app():
    while True:
        choice = show_menu()
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please choose again.")

# Run the To-Do List app
if __name__ == "__main__":
    run_app()

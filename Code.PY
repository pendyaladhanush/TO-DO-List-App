import os

# File to store tasks
TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASK_FILE, "w") as file:
        file.write("\n".join(tasks))

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def complete_task(tasks):
    """Mark a task as complete."""
    display_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            completed_task = tasks.pop(task_num - 1)
            print(f"Task '{completed_task}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do list app."""
    tasks = load_tasks()
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Complete a task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

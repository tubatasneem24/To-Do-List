def add_task(task):
    """Add a task to the todo list."""
    with open('todos.txt', 'a') as file:
        file.write(task + '\n')

def view_tasks():
    """View all tasks in the todo list."""
    try:
        with open('todos.txt', 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks in the list.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found. Add some tasks first.")

def remove_task(index):
    """Remove a task by index."""
    try:
        with open('todos.txt', 'r') as file:
            tasks = file.readlines()
        if index < 1 or index > len(tasks):
            print("Invalid index.")
            return
        with open('todos.txt', 'w') as file:
            for idx, task in enumerate(tasks, 1):
                if idx != index:
                    file.write(task)
        print("Task removed successfully.")
    except FileNotFoundError:
        print("No tasks file found.")

def main():
    """Main function to run the todo list manager."""
    while True:
        print("\nTodo List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                index = int(input("Enter the task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

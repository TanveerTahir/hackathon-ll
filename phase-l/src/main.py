"""
Main entry point for the Todo application.
Implements the main loop and menu navigation.
"""
try:
    from .storage import TaskStore
    from .services import TodoService
    from .cli import TodoCLI
except ImportError:
    from storage import TaskStore
    from services import TodoService
    from cli import TodoCLI


def main():
    """Main function to run the Todo application."""
    # Initialize the task store and service layer, then CLI
    task_store = TaskStore()
    todo_service = TodoService(task_store)
    cli = TodoCLI(todo_service)

    print("Welcome to the Todo Application!")

    while True:
        # Display menu
        cli.display_menu()

        # Get user choice
        try:
            choice = input("Please select an option (1-6): ").strip()

            if choice == "1":
                cli.add_task()
            elif choice == "2":
                cli.view_tasks()
            elif choice == "3":
                cli.update_task()
            elif choice == "4":
                cli.delete_task()
            elif choice == "5":
                cli.toggle_task_complete()
            elif choice == "6":
                print("Thank you for using the Todo Application. Goodbye!")
                break
            else:
                print("Invalid option. Please select a number between 1 and 6.")
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
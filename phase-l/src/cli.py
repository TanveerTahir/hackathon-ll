"""
Command-Line Interface for the Todo application.
Handles user input and output.
"""
from typing import Optional
try:
    from .models import Task
    from .services import TodoService
except ImportError:
    from models import Task
    from services import TodoService


class TodoCLI:
    """Handles the command-line interface for the Todo application."""

    def __init__(self, todo_service: TodoService):
        """
        Initialize the CLI with a todo service.

        Args:
            todo_service: The TodoService instance to use
        """
        self.todo_service = todo_service

    def display_menu(self):
        """Display the main menu options."""
        print("\n=== Todo Application ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Exit")
        print("========================")

    def get_user_input(self, prompt: str) -> str:
        """
        Get input from the user with a prompt.

        Args:
            prompt: The prompt to display

        Returns:
            User input string
        """
        return input(prompt).strip()

    def get_task_id_input(self) -> Optional[int]:
        """
        Get a task ID from user input, with validation.

        Returns:
            Integer task ID if valid, None otherwise
        """
        try:
            id_str = self.get_user_input("Enter task ID: ").strip()
            if not id_str:
                print("Task ID cannot be empty.")
                return None
            task_id = int(id_str)
            if task_id <= 0:
                print("Task ID must be a positive integer.")
                return None
            return task_id
        except ValueError:
            print("Please enter a valid integer for the task ID.")
            return None

    def add_task(self):
        """Handle adding a new task."""
        title = self.get_user_input("Enter task title: ")
        if not title.strip():
            print("Error: Task title cannot be empty.")
            return

        description = self.get_user_input("Enter task description (optional): ")

        try:
            task = self.todo_service.add_task(title, description)
            print(f"Task '{task.title}' added successfully with ID {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def view_tasks(self):
        """Handle viewing all tasks."""
        tasks = self.todo_service.get_all_tasks()

        if not tasks:
            print("\nNo tasks found.")
            return

        print("\n--- Your Tasks ---")
        for task in tasks:
            status_symbol = "✅" if task.completed else "❌"
            print(f"[{task.id}] {task.title} — ({status_symbol})")
            if task.description:
                print(f"{task.description}")
            print("-" * 30)

    def update_task(self):
        """Handle updating a task."""
        task_id = self.get_task_id_input()
        if task_id is None:
            return

        # Check if task exists
        existing_task = self.todo_service.get_task(task_id)
        if not existing_task:
            print(f"Error: Task with ID {task_id} not found.")
            return

        title = self.get_user_input(f"Enter new title (current: '{existing_task.title}'): ")
        description = self.get_user_input(f"Enter new description (current: '{existing_task.description}'): ")

        # If user pressed enter without typing, keep the original value
        if not title:
            title = existing_task.title
        if not description:
            description = existing_task.description

        try:
            updated_task = self.todo_service.update_task(task_id, title, description)
            if updated_task:
                print(f"Task {task_id} updated successfully.")
            else:
                print("Error: Failed to update task (invalid input).")
        except Exception as e:
            print(f"Error updating task: {e}")

    def delete_task(self):
        """Handle deleting a task."""
        task_id = self.get_task_id_input()
        if task_id is None:
            return

        success = self.todo_service.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Error: Task with ID {task_id} not found.")

    def toggle_task_complete(self):
        """Handle marking a task as complete/incomplete."""
        task_id = self.get_task_id_input()
        if task_id is None:
            return

        success = self.todo_service.toggle_task_complete(task_id)
        if success:
            task = self.todo_service.get_task(task_id)
            status = "completed" if task.completed else "marked as incomplete"
            print(f"Task {task_id} {status}.")
        else:
            print(f"Error: Task with ID {task_id} not found.")
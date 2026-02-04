"""
Business logic service for the Todo application.
Coordinates between models and storage.
"""
from typing import List, Optional
try:
    from .models import Task
    from .storage import TaskStore
except ImportError:
    from models import Task
    from storage import TaskStore


class TodoService:
    """Business logic layer that coordinates between models and storage."""

    def __init__(self, task_store: TaskStore):
        """
        Initialize the service with a task store.

        Args:
            task_store: The TaskStore instance to use
        """
        self.task_store = task_store

    def add_task(self, title: str, description: str = "") -> Optional[Task]:
        """
        Add a new task with validation.

        Args:
            title: Task title (must not be empty)
            description: Task description (optional)

        Returns:
            Created Task object if successful, None otherwise
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        return self.task_store.add_task(title, description)

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.

        Returns:
            List of all tasks
        """
        return self.task_store.get_all_tasks()

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        return self.task_store.get_task(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Update a task with validation.

        Args:
            task_id: The ID of the task to update
            title: New title (optional, but if provided cannot be empty)
            description: New description (optional)

        Returns:
            Updated Task object if successful, None otherwise
        """
        # Validate title if provided
        if title is not None and not title.strip():
            raise ValueError("Title cannot be empty")

        return self.task_store.update_task(task_id, title, description)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if not found
        """
        return self.task_store.delete_task(task_id)

    def toggle_task_complete(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if task was toggled, False if not found
        """
        return self.task_store.toggle_complete(task_id)
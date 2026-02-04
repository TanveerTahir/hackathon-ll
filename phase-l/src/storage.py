"""
In-memory storage for the Todo application.
Manages the collection of tasks with required operations.
"""
from typing import Dict, List, Optional
try:
    from .models import Task
except ImportError:
    from models import Task


class TaskStore:
    """Manages in-memory storage of tasks."""

    def __init__(self):
        """Initialize an empty task store."""
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def _generate_next_id(self) -> int:
        """Generate a unique ID for a new task."""
        current_id = self._next_id
        self._next_id += 1
        # Make sure the ID is not already taken (though unlikely)
        while current_id in self._tasks:
            current_id = self._next_id
            self._next_id += 1
        return current_id

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Create and add a new task to the store.

        Args:
            title: Task title
            description: Task description (optional)

        Returns:
            Created Task object
        """
        task_id = self._generate_next_id()
        task = Task(task_id, title, description)
        self._tasks[task_id] = task
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the store.

        Returns:
            List of all tasks
        """
        return list(self._tasks.values())

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        return self._tasks.get(task_id)

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task by ID.

        Args:
            task_id: The ID of the task to remove

        Returns:
            True if task was removed, False if task was not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Modify an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            Updated Task object if found, None otherwise
        """
        task = self.get_task(task_id)
        if task:
            try:
                task.update(title=title, description=description)
                return task
            except ValueError:
                # If validation fails, return None
                return None
        return None

    def toggle_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete or incomplete.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if task was found and toggled, False otherwise
        """
        task = self.get_task(task_id)
        if task:
            task.update(completed=not task.completed)
            return True
        return False
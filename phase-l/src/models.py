"""
Task data model for the Todo application.
Contains the Task class with required fields.
"""
from datetime import datetime
from typing import Optional


class Task:
    """Represents a single todo task."""

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            id: Unique identifier for the task
            title: Short title/description of the task
            description: Longer description of the task (optional)
            completed: Whether the task is completed (default: False)
        """
        if not title.strip():
            raise ValueError("Title cannot be empty")

        self.id = id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.completed = completed
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, title: Optional[str] = None, description: Optional[str] = None, completed: Optional[bool] = None):
        """
        Update task fields and update the updated_at timestamp.

        Args:
            title: New title (optional)
            description: New description (optional)
            completed: New completion status (optional)
        """
        if title is not None:
            if not title.strip():
                raise ValueError("Title cannot be empty")
            self.title = title.strip()

        if description is not None:
            self.description = description.strip() if description else ""

        if completed is not None:
            self.completed = completed

        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """Convert task to dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    def __str__(self):
        """String representation of the task."""
        status = "✅" if self.completed else "❌"
        return f"[{self.id}] {self.title} — ({status})\n{self.description}"
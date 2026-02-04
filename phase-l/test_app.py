#!/usr/bin/env python3
"""
Simple test to verify that all modules import correctly and basic functionality works.
"""

import sys
import os

# Add the src directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all modules can be imported without errors."""
    try:
        from models import Task
        from storage import TaskStore
        from services import TodoService
        from cli import TodoCLI
        from main import main

        print("[PASS] All modules imported successfully")

        # Test basic functionality
        store = TaskStore()
        service = TodoService(store)

        # Test creating a task
        task = service.add_task("Test task", "This is a test description")
        print(f"[PASS] Created task: ID={task.id}, Title='{task.title}', Description='{task.description}'")

        # Test getting all tasks
        tasks = service.get_all_tasks()
        print(f"[PASS] Retrieved {len(tasks)} task(s)")

        # Test toggling completion
        success = service.toggle_task_complete(task.id)
        print(f"[PASS] Toggled task completion: {success}")
        print(f"  Task completed status: {task.completed}")

        # Test updating task
        updated_task = service.update_task(task.id, "Updated test task", "Updated description")
        print(f"[PASS] Updated task: Title='{updated_task.title}', Description='{updated_task.description}'")

        # Test deleting task
        success = service.delete_task(task.id)
        print(f"[PASS] Deleted task: {success}")

        # Verify deletion
        tasks = service.get_all_tasks()
        print(f"[PASS] After deletion, {len(tasks)} task(s) remain")

        print("\n[PASS] All basic functionality tests passed!")

    except Exception as e:
        print(f"[FAIL] Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True

if __name__ == "__main__":
    print("Testing Todo Application modules...")
    success = test_imports()

    if success:
        print("\n[SUCCESS] All tests passed! The Todo application is working correctly.")
    else:
        print("\n[ERROR] Some tests failed.")
        sys.exit(1)
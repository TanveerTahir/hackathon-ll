# Todo API Contract

## Overview

This contract defines the interface between the CLI layer and the TodoService. Although currently implemented as direct method calls, this contract enables future replacement with REST APIs, MCP tools, or other interfaces.

## Service Interface: TodoService

### Methods

#### create_task(title: string): Promise<Task>
- **Purpose**: Creates a new task with the given title
- **Input**:
  - title: string (non-empty, trimmed)
- **Output**: Task object with all required fields populated
- **Errors**:
  - Throws error if title is empty or contains only whitespace
- **Side Effects**: Task is persisted in repository, timestamps are set

#### list_tasks(): Promise<Task[]>
- **Purpose**: Retrieves all tasks in the system
- **Input**: None
- **Output**: Array of all Task objects, sorted by creation date (oldest first)
- **Errors**: None (returns empty array if no tasks exist)
- **Side Effects**: None

#### complete_task(id: string): Promise<Task | null>
- **Purpose**: Marks a task as completed
- **Input**:
  - id: string (valid task ID)
- **Output**: Updated Task object, or null if ID not found
- **Errors**: None (returns null for invalid IDs)
- **Side Effects**: Updates the task's completion status and updated_at timestamp

#### update_task(id: string, new_title: string): Promise<Task | null>
- **Purpose**: Updates the title of an existing task
- **Input**:
  - id: string (valid task ID)
  - new_title: string (non-empty, trimmed)
- **Output**: Updated Task object, or null if ID not found
- **Errors**:
  - Throws error if new_title is empty or contains only whitespace
  - Returns null if ID not found
- **Side Effects**: Updates the task's title and updated_at timestamp

#### delete_task(id: string): Promise<boolean>
- **Purpose**: Removes a task from the system
- **Input**:
  - id: string (valid task ID)
- **Output**: Boolean indicating whether deletion occurred (true = deleted, false = not found)
- **Errors**: None
- **Side Effects**: Task is removed from repository

## Data Contracts

### Task Object
```
{
  id: string,
  title: string,
  completed: boolean,
  created_at: Date,
  updated_at: Date
}
```

### Validation Rules
- id: Must be unique across all tasks, immutable after creation
- title: Must not be empty or contain only whitespace, max length 500 characters
- completed: Boolean value, defaults to false
- created_at: Date object, immutable after creation
- updated_at: Date object, updated whenever the task is modified

## Error Handling Contract

All methods follow the same error handling pattern:
- Validation errors (e.g., empty titles) throw exceptions with descriptive messages
- Resource not found (e.g., invalid IDs) returns null or false instead of throwing
- Unexpected errors propagate up to be handled by the CLI layer

## Expected Response Times

All operations should complete within 100ms under normal conditions with fewer than 10,000 tasks in memory.

## Thread Safety

This contract assumes single-threaded execution (typical for CLI applications). No explicit thread safety measures are required for Phase I implementation.
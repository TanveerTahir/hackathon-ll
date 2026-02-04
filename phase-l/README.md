# Phase I — In-Memory Python Console Todo App

A command-line todo application built in Python with in-memory storage following Spec-Driven Development principles.

## Features

- Add new tasks with title and description
- View all tasks with completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- In-memory storage (no database required)

## Architecture

The application follows a layered architecture:

- **Models** (`src/models.py`): Task entity definition
- **Storage** (`src/storage.py`): In-memory task persistence
- **Services** (`src/services.py`): Business logic layer
- **CLI** (`src/cli.py`): User interface layer
- **Main** (`src/main.py`): Application entry point

## Requirements

- Python 3.11+

## Installation

No installation required - the application uses only built-in Python libraries.

## Usage

Run the application:
```bash
python -m src.main
```

The application will present a menu with the following options:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Exit

## Design Principles

- **Separation of Concerns**: Clear separation between models, storage, business logic, and presentation
- **Deterministic Behavior**: Same command sequences produce the same results
- **Error Handling**: Graceful handling of invalid inputs and edge cases
- **Spec Compliance**: Strict adherence to the original specification

## Testing

Run the test suite:
```bash
python test_app.py
```
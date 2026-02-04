# Implementation Tasks: Todo Engine

**Feature**: Todo Engine
**Branch**: `001-todo-engine`
**Input**: Feature specification from `/specs/001-todo-engine/spec.md`

## Task Dependencies

User Story 1 must be completed before User Story 2, 3, 4, and 5.
User Story 2, 3, and 4 are independent of each other.
User Story 5 can be implemented in parallel with Stories 2, 3, and 4.

## Parallel Execution Examples

- User Story 2 (View Tasks) and User Story 3 (Complete Tasks) can be developed simultaneously
- User Story 4 (Update Tasks) and User Story 5 (Delete Tasks) can be developed simultaneously
- Models and Repository layer can be developed in parallel with Service layer implementation

## Implementation Strategy

The implementation follows the MVP-first approach, where User Story 1 (Add Tasks) is implemented first to establish the core architecture. This enables rapid iteration and early validation of the foundational components. Subsequent user stories build incrementally on this foundation.

---

## Phase 1: Project Setup

- [x] T001 Create project structure with src directory containing main.py, models.py, storage.py, and cli.py
- [x] T002 Initialize project dependencies and configuration files as needed

## Phase 2: Foundational Components

- [x] T010 [P] Implement Task data model in src/models.py with id, title, description, completed fields
- [x] T011 [P] Implement in-memory TaskStore in src/storage.py with required methods
- [x] T012 [P] [US1] Create TodoService in src/services.py that connects models and storage
- [x] T013 [P] [US1] Implement CLI menu system in src/cli.py that displays numbered options

## Phase 3: [US1] Add New Tasks

Goal: User can create new todo items with a title and description.

Independent Test: Run the CLI, select "Add Task", enter a title and description, and verify a new task appears in the system with a unique ID.

- [x] T020 [P] [US1] Implement add_task method in TodoService that validates title is not empty
- [x] T021 [P] [US1] Implement add_task functionality in TaskStore to generate unique IDs
- [x] T022 [P] [US1] Implement Task model validation to reject empty titles
- [x] T023 [US1] Create CLI function to prompt for title and description
- [x] T024 [US1] Connect CLI add_task function to TodoService
- [x] T025 [US1] Display confirmation message after successful task creation
- [x] T026 [US1] Implement error handling for empty title validation

## Phase 4: [US2] View All Tasks

Goal: User can see all tasks with their status and details.

Independent Test: Add several tasks, then run the "View Tasks" command to see all tasks displayed in a readable format.

- [x] T030 [P] [US2] Implement get_all_tasks method in TodoService
- [x] T031 [P] [US2] Implement get_all_tasks functionality in TaskStore
- [x] T032 [US2] Create CLI function to display all tasks in format: [ID] Title — (Completed ❌ or ✔️) Description
- [x] T033 [US2] Format task display with appropriate symbols for completion status
- [x] T034 [US2] Handle case where no tasks exist

## Phase 5: [US3] Mark Tasks Complete

Goal: User can mark tasks as completed to track their progress.

Independent Test: Add a task, note its ID, run the "Mark Task Complete" command with the ID, and verify the task is marked as completed.

- [x] T040 [P] [US3] Implement toggle_complete method in TodoService
- [x] T041 [P] [US3] Implement toggle_complete functionality in TaskStore
- [x] T042 [US3] Create CLI function to prompt for task ID and mark as complete
- [x] T043 [US3] Connect CLI toggle function to TodoService
- [x] T044 [US3] Implement error handling for invalid task IDs

## Phase 6: [US4] Update Task Information

Goal: User can modify the title and description of existing tasks.

Independent Test: Add a task, update its title and description, and verify the changes are reflected when viewing tasks.

- [x] T050 [P] [US4] Implement update_task method in TodoService
- [x] T051 [P] [US4] Implement update_task functionality in TaskStore
- [x] T052 [US4] Create CLI function to prompt for task ID, new title, and new description
- [x] T053 [US4] Connect CLI update function to TodoService
- [x] T054 [US4] Implement error handling for invalid task IDs and empty titles

## Phase 7: [US5] Delete Tasks

Goal: User can remove tasks that are no longer needed.

Independent Test: Add a task, delete it, and verify it no longer appears in the task list.

- [x] T060 [P] [US5] Implement delete_task method in TodoService
- [x] T061 [P] [US5] Implement delete_task functionality in TaskStore
- [x] T062 [US5] Create CLI function to prompt for task ID and delete the task
- [x] T063 [US5] Connect CLI delete function to TodoService
- [x] T064 [US5] Implement error handling for invalid task IDs

## Phase 8: [US1] CLI Menu Navigation

Goal: User can navigate the CLI menu system to access all functionality.

- [x] T070 [US1] Implement main loop in src/main.py that continuously shows the menu
- [x] T071 [US1] Connect all CLI functions to the numbered menu options (1-6)
- [x] T072 [US1] Implement "Exit" functionality that terminates the application
- [x] T073 [US1] Handle invalid menu selections with appropriate error messages

## Phase 9: Error Handling & Validation

Goal: System handles edge cases gracefully and never crashes.

- [x] T080 Implement input validation for all user-entered data
- [x] T081 Handle non-numeric inputs when numbers are expected
- [x] T082 Display appropriate error messages for invalid IDs
- [x] T083 Prevent application crashes on unexpected inputs
- [x] T084 Validate that all required functionality meets Phase-1 compliance requirements

## Phase 10: Final Integration & Testing

Goal: All components work together as a cohesive application.

- [x] T090 Conduct end-to-end testing of all functionality
- [x] T091 Verify the application runs correctly with `python main.py`
- [x] T092 Test that all 5 Basic features work as specified
- [x] T093 Verify in-memory data persistence throughout session
- [x] T094 Validate compliance with all requirements in the specification
- [x] T095 Clean up code and ensure adherence to project structure requirements
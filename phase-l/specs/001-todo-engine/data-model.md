# Data Model: Todo Engine

## Task Entity

### Fields

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| id | string | Unique immutable identifier | Auto-generated, never changes, globally unique |
| title | string | Short human-readable description | Cannot be empty, can be updated |
| completed | boolean | Whether the task is done | Default: false, can be updated |
| created_at | Date | When task was created | Immutable after creation |
| updated_at | Date | When task was last modified | Updates on any modification |

### Validation Rules

1. **Title cannot be empty**: All operations that create or update a task must validate that the title contains at least one non-whitespace character.
2. **IDs must be unique**: The system must prevent duplicate IDs in the repository.
3. **Creation time is immutable**: The `created_at` field cannot be changed after initial creation.
4. **Updated time changes on modification**: The `updated_at` field must be updated whenever a task is modified.
5. **Completing a task updates timestamps**: When a task is marked as completed, `completed` changes to true and `updated_at` is updated.

### State Transitions

- **Initial State**: `completed: false` when task is created
- **Completion**: `completed: false` → `completed: true` when task is marked complete
- **Title Update**: `title: "old"` → `title: "new"` when task title is updated
- **Timestamp Update**: `updated_at: timestamp` changes on any modification (completion, title update)

## TaskRepository Interface

### Operations

| Operation | Parameters | Return Type | Description |
|-----------|------------|-------------|-------------|
| save | task: Task | Task | Saves a task to the repository |
| get_by_id | id: string | Task \| null | Retrieves a task by ID |
| list_all | none | Task[] | Returns all tasks in the repository |
| update | task: Task | Task \| null | Updates an existing task |
| delete | id: string | boolean | Removes a task by ID, returns success status |

### Constraints

1. **Save**: Must validate that the task has a valid ID before saving
2. **Get by ID**: Returns null if ID does not exist
3. **List all**: Returns empty array if no tasks exist
4. **Update**: Validates that the task exists before updating, returns null if not found
5. **Delete**: Returns false if ID does not exist, true if successfully deleted

## Relationships

### Task → Timestamps
- Each Task has one `created_at` timestamp (immutable)
- Each Task has one `updated_at` timestamp (mutable)

### TaskRepository → Tasks
- One TaskRepository contains zero or more Tasks
- TaskRepository provides CRUD operations for Tasks
- TaskRepository maintains uniqueness of Task IDs

## Domain Invariants

1. **Identity Integrity**: Each Task maintains its ID throughout its lifecycle
2. **Temporal Consistency**: `created_at` ≤ `updated_at` always holds true
3. **State Completeness**: Every Task has a completion state (true/false)
4. **Repository Uniqueness**: No two Tasks in the same Repository have the same ID
5. **Data Completeness**: Every Task has all required fields populated
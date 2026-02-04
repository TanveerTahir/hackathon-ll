# Quickstart Guide: Todo Engine

## Prerequisites

- Node.js v18 or higher
- npm or yarn package manager

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install dependencies:
```bash
npm install
```

3. Build the project:
```bash
npm run build
```

## Running the Application

Start the Todo CLI application:
```bash
npm start
```

Or run directly with ts-node:
```bash
npx ts-node src/cli/todo.cli.ts
```

## Available Commands

Once the application is running, you can use the following commands:

### Add a new task
```
add "Your task title here"
```

### List all tasks
```
list
```

### Complete a task
```
complete <task-id>
```

### Update a task title
```
update <task-id> "New title"
```

### Delete a task
```
delete <task-id>
```

### Exit the application
```
exit
```

## Example Session

```
> add "Buy groceries"
Task 'Buy groceries' created with ID: 12345
> add "Walk the dog"
Task 'Walk the dog' created with ID: 67890
> list
1. [ ] 12345: Buy groceries (created: 2023-01-01, updated: 2023-01-01)
2. [ ] 67890: Walk the dog (created: 2023-01-01, updated: 2023-01-01)
> complete 12345
Task 12345 marked as complete
> list
1. [x] 12345: Buy groceries (created: 2023-01-01, updated: 2023-01-02)
2. [ ] 67890: Walk the dog (created: 2023-01-01, updated: 2023-01-01)
> exit
Goodbye!
```

## Development

### Running tests
```bash
npm test
```

### Building for production
```bash
npm run build
```

### Linting
```bash
npm run lint
```

## Troubleshooting

- If you get an error about missing dependencies, run `npm install` again
- If the application won't start, check that Node.js v18+ is installed (`node --version`)
- For any command errors, ensure you're following the exact syntax shown above
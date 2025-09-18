# Python To-Do Application

A command-line To-Do List Application built with Python that allows users to manage their tasks through an interactive CLI interface.

## Features

- **Add Tasks**: Create new to-do items with name and description
- **View Tasks**: Display detailed information about specific tasks
- **Delete Tasks**: Remove tasks from the collection
- **Input Validation**: Comprehensive error handling for invalid inputs
- **User-Friendly Interface**: Color-coded success/error messages

## Project Structure

```
python-todo/
├── main.py              # Main application entry point and CLI interface
├── todo_item.py         # TodoItem class with name and description properties
├── todo_collection.py   # TodoCollection class managing the list of tasks
├── print_utilities.py   # Utility functions for formatted output
└── venv/               # Virtual environment (not included in repository)
```
**Follow the interactive prompts**:
   - Enter your name when prompted
   - Use the following commands:
     - `add <name> <description>` - Add a new task
     - `view <name>` - View task details
     - `delete <name>` - Delete a task
     - `quit` - Exit the application

## Usage Examples

```
> add "Buy groceries" "Milk, bread, eggs"
> view "Buy groceries"
> delete "Buy groceries"
> quit
```

## Error Handling

The application includes comprehensive error handling for:
- Invalid command syntax
- Non-existent tasks
- Empty task collections
- Invalid menu selections
- Duplicate task names


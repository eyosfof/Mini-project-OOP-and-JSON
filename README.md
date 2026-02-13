# OOP-Based CLI Todo App

## Project Overview

This is a Command Line Interface (CLI) Todo Application built using
Object-Oriented Programming (OOP) principles. All tasks are stored in a
local `todos.json` file using JSON serialization and deserialization.

## Features

-   Add Todo
-   View Todos (ID, Title, Completion Status)
-   Update Todo (Change title or completion status)
-   Delete Todo (Using ID)
-   Persistent Data Storage (JSON)

## How to Run

1.  Make sure Python 3 is installed.

2.  Clone the repository:

    ``` bash
    git clone <your-repository-link>
    cd oop_cli_todo_app
    ```

3.  Run the application:

    ``` bash
    python main.py
    ```

## JSON to Object Conversion

### Serialization

Each `Task` object is converted into a dictionary using the `to_dict()`
method. Then the list of dictionaries is saved into `todos.json` using
`json.dump()`.

### Deserialization

When the app starts, it loads `todos.json`. Each dictionary is converted
back into a `Task` object using the `from_dict()` static method.

This ensures data persistence even after restarting the program.

## Example Commit Messages

-   Initial project setup
-   Implemented Task class
-   Added JSON serialization and deserialization
-   Implemented update and delete functionality
-   Added README and documentation

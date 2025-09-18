"""
To-Do App

Requirements:
- Welcomes user
- Display menu with options for tasks and app:
    - add
    - view
    - delete
    - quit app
- Tasks stored in Python List
- Use input() to get user inputs
- Ensure proper input validation
    - Alert user on invalid inputs
    - Alert user if no tasks to view
    - Alert user if they try to delete a taks that doesn't exist
    - Alert user if they choose main-menu item that doesn't exist
"""

# NOTE: There is some pretty lazy O(N) going on here but we can probably use
# hashing to improve the efficiency by quite a bit once the todo-lists start
# to get really long.

# custom
from todo_collection import TodoCollection
from print_utilities import display_user_error, display_success

# package
from typing import List
import time


def welcome_user() -> str:
    """Welcome message for user"""
    print("Hello, and welcome to your to-do tracker!")
    username: str = input("Please type your name -> ")
    return username


def take_user_input() -> list[str]:
    """Ask user what they would like to do and take their input"""
    print("What would you like to do?")
    print("1. add todo item -> add (name) (description)")
    print("2. view todo item details -> view (name)")
    print("3. delete todo item -> delete (name)")
    print("4. Quit the app -> quit")

    user_input = input("> ").strip()
    return user_input.split(" ", 2)


def goodbye_and_exit():
    print("Goodbye!")
    time.sleep(1)
    exit()


def parse_and_perform_user_input(
    user_input: List[str], todo_collection: TodoCollection
):
    """Matches user input to appropriate class function from TodoCollection and executes"""
    command, *args = user_input

    # NOTE: Uggo but worko
    try:
        match command:
            case "add":
                if len(args) != 2:
                    display_user_error("Proper 'add' usage: add (name) (description)")
                else:
                    res = todo_collection.add_todo_item(args[0], args[1])
                    display_success(res)
            case "view":
                if len(args) != 1:
                    display_user_error("Proper 'view' usage: view (name)")
                else:
                    res = todo_collection.view_todo_item(args[0])
                    display_success(res)
            case "delete":
                if len(args) != 1:
                    display_user_error("Proper 'delete' usage: delete (name)")
                else:
                    res = todo_collection.delete_todo_item(args[0])
                    display_success(res)
            case "quit":
                if len(args) > 0:
                    display_user_error("Proper 'quit' usage: quit (no args)")
                else:
                    goodbye_and_exit()
            case _:
                display_user_error("Please provide a valid input!")
    except ValueError as e:
        display_user_error(f"{str(e)}")


def main():
    todo_collection = TodoCollection()

    while True:
        user_input = take_user_input()
        parse_and_perform_user_input(user_input, todo_collection)


if __name__ == "__main__":
    main()

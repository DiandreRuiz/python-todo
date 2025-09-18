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

from todo_collection import TodoCollection
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
                    print()
                    print("\033[91mProper 'add' usage: add (name) (description)\033[0m")
                    print()
                else:
                    todo_collection.add_todo_item(args[0], args[1])
            case "view":
                if len(args) != 1:
                    print()
                    print("\033[91mProper 'view' usage: view (name)\033[0m")
                    print()
                else:
                    todo_collection.view_todo_item(args[0])
            case "delete":
                if len(args) != 1:
                    print()
                    print("\033[91mProper 'delete' usage: delete (name)\033[0m")
                    print()
                else:
                    todo_collection.delete_todo_item(args[0])
            case "quit":
                if len(args) > 0:
                    print()
                    print("\033[91mProper 'quit' usage: quit (no args)\033[0m")
                    print()
                else:
                    goodbye_and_exit()
            case _:
                print("\033[91mPlease provide a valid input!\033[0m")
                print()
    except ValueError as e:
        print(f"\033[91m{str(e)}\033[0m")
        print()


def main():
    todo_collection = TodoCollection()

    while True:
        user_input = take_user_input()
        parse_and_perform_user_input(user_input, todo_collection)


if __name__ == "__main__":
    main()

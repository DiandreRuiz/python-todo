from typing import List
from todo_item import TodoItem


class TodoCollection:
    def __init__(self, collection=[]):
        self._collection: List[TodoItem] = collection

    def add_todo_item(self, name: str, description: str):
        """Adds TodoItem to _collection for this Collection Obj"""
        self._collection.append(TodoItem(name, description))
        print(f"Added todo item '{name}'")

    def view_todo_item(self, name: str) -> TodoItem:
        """Returns TodoItem based on name"""
        for todo_item in self._collection:
            if todo_item.name == name:
                print("----- To-Do Item Info -----")
                print(f"Name: {todo_item.name}")
                print(f"Description: {todo_item.description}")
        raise ValueError(
            "No todo list exists with that name. Did you double check capitalization?"
        )

    def delete_todo_item(self, name: str):
        """Removes a TodoItem from this _collection based on name"""
        # Check if any item matches before filtering
        if not any(todo.name == name for todo in self._collection):
            raise ValueError(f"No todo item found with name: {name}")

        # Keep everything except the matching item(s)
        self._collection = [todo for todo in self._collection if todo.name != name]

        print(f"Deleted todo item '{name}'")

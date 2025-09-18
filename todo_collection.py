from typing import List
from todo_item import TodoItem
from print_utilities import display_success


class TodoCollection:
    def __init__(self, collection=[]):
        self._collection: List[TodoItem] = collection

    def add_todo_item(self, name: str, description: str) -> str:
        """Adds TodoItem to _collection for this Collection Obj"""
        if any(todo.name == name for todo in self._collection):
            raise ValueError(f"To-Do item with name {name} already exists!")
        self._collection.append(TodoItem(name, description))
        message = f"Added todo item '{name}'"

        return message

    def view_todo_item(self, name: str) -> str:
        """Returns TodoItem based on name"""
        for todo_item in self._collection:
            if todo_item.name == name:
                message = f"""
        ----- To-Do Item Info -----
        Name:
        {todo_item.name}
        Description:
        {todo_item.description}
        """

                return message

        raise ValueError(
            f"""No To-Do item found named: '{name}'
        Did you double check capitalization?"""
        )

    def delete_todo_item(self, name: str) -> str:
        """Removes a TodoItem from this _collection based on name"""

        # Check if any item matches before filtering
        if not any(todo.name == name for todo in self._collection):
            raise ValueError(
                f"""No To-Do item found named: '{name}'
        Nothing to delete!"""
            )

        # Keep everything except the matching item(s)
        starting_length = len(self._collection)
        self._collection = [todo for todo in self._collection if todo.name != name]

        message = f"""
        Deleted To-Do item '{name}'
        Number of To-Do items: {starting_length} items -> {len(self._collection)} items
        """

        return message

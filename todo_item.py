class TodoItem:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @description.setter
    def description(self, value: str):
        if not value:
            raise ValueError("Description cannot be empty")
        self._description = value
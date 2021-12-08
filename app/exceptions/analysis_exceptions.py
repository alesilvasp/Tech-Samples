
class InvalidKeysError(Exception):
    def __init__(self) -> None:
        self.message = {'error': 'One or more invalid keys were given.'}, 400
        super().__init__(self.message)

class MissingKeysError(Exception):
    def __init__(self) -> None:
        self.message = {'error': 'One or more keys are missing.'}, 400
        super().__init__(self.message)

class TypeError(Exception):
    def __init__(self) -> None:
        self.message = {'error': 'One or more keys have the wrong type.'}, 400
        super().__init__(self.message)

class ForeignKeyNotFoundError(Exception):
    def __init__(self) -> None:
        self.message = {'error': 'One or more foreign keys were not found.'}, 404
        super().__init__(self.message)
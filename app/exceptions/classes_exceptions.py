class InvalidInputDataError(Exception):
    def __init__(self):

        self.message = {
            "error": "Invalid input data key, key must be 'name'"
        }, 400

        super().__init__(self.message)


class InvalidTypeInputDataError(Exception):
    def __init__(self):

        self.message = {
            "error": "Invalid input data values, name must be of type string and admin_id must be of type int"
        }, 400

        super().__init__(self.message)


class ClassNotFoundError(Exception):
    def __init__(self):

        self.message = {
            "error": "Class not found"
        }, 404

        super().__init__(self.message)


class ConflictError(Exception):
    def __init__(self):

        self.message = {
            'error': 'Class already exists'
        }, 409

        super().__init__(self.message)


class InvalidInputDataError(Exception):

    def __init__(self):

        self.message = {
            "error": "Invalid input data keys, avaliable keys: name, admin_id"
        }, 400

        super().__init__(self.message)


class InvalidTypeInputDataError(Exception):

    def __init__(self):

        self.message = {
            "error": "invalid input data values, name must be of type string and admin_id must be of type int"
        }, 400

        super().__init__(self.message)


class ClassNotFoundError(Exception):

    def __init__(self):

        self.message = {
            "error": "class not found"
        }, 404

        super().__init__(self.message)

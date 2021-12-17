class InvalidInputDataError(Exception):

    def __init__(self):

        self.message = {
            "error": "Invalid input data keys, avaliable keys: name, class_id"
        }, 400

        super().__init__(self.message)


class InvalidTypeInputDataError(Exception):

    def __init__(self):

        self.message = {
            "error": "Invalid input data values, name must be of type string and class_id must be of type int"
        }, 400

        super().__init__(self.message)


class InvalidUpdateDataError(Exception):

    def __init__(self):

        self.message = {
            "error": "Only the key name must be informed and it must be of type string"
        }, 400

        super().__init__(self.message)


class TypeNotFoundError(Exception):

    def __init__(self):

        self.message = {
            "error": "Type not found"
        }, 404

        super().__init__(self.message)

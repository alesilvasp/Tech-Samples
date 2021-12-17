class InvalidInputDataError(Exception):

    def __init__(self):

        self.message = {
            "error": "Invalid input data"
        }, 400

        super().__init__(self.message)


class ParametersNotFoundError(Exception):

    def __init__(self):

        self.message = {
            "error": "Parameters not found"
        }, 404

        super().__init__(self.message)


class InvalidDataTypeError(Exception):

    def __init__(self):

        self.message = {
            "error": "Invalid data type"
        }

        super().__init__(self.message)

class DataContentError(Exception):
    def __init__(self, key):

        self.message = {'error': f'Verify key: {key}'}, 400

        super().__init__(self.message)


class EmailFormatError(Exception):
    def __init__(self):

        self.message = {'error': 'Not valid email format'}, 400

        super().__init__(self.message)


class InvalidUpdateDataError(Exception):

    def __init__(self):

        self.message = {
            'error': 'Only the key password must be informed and it must be of type string'
        }, 400

        super().__init__(self.message)


class EmailConflictError(Exception):

    def __init__(self):

        self.message = {'error': 'Email already registred'}, 409

        super().__init__(self.message)

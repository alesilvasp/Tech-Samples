class DataContentError(Exception):
    def __init__(self, key):

        self.message = {'error': f'Verify key: {key}'}, 400

        super().__init__(self.message)


class EmailFormatError(Exception):
    def __init__(self):

        self.message = {'error': 'Not valid email format'}, 400

        super().__init__(self.message)

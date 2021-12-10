class DataContentError(Exception):
    def __init__(self, key):
        
        self.message = {'error': f'Verify key: {key}'}, 400
        
        super().__init__(self.message)


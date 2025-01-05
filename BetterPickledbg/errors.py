class PickleError(Exception):
    pass

class PicklingError(PickleError):
    pass

class UnpicklingError(PickleError):
    pass

class ValidationError(Exception):
    pass

class _Stop(Exception):
    def __init__(self, value):
        self.value = value
        
class _Exit(Exception):
    def __init__(self, value):
        self.value = value
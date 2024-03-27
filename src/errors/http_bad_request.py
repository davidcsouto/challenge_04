class HttpBadRequestError(Exception):  # all class that inherits superclass Exception becomes a class to exception
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'BadRequest'
        self.status_code = 400

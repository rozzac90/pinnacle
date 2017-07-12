
class PinnacleError(Exception):
    pass


class ApiError(PinnacleError):
    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code
        try:
            if type(self.response) == dict:
                self.message = self.response.get('message')
                self.details = self.response.get('code')
            else:
                self.message = self.response.json()['message']
                self.details = self.response.json()['code']
        except KeyError:
            self.message = 'UNKNOWN'
            self.details = None
        super(ApiError, self).__init__(self.message)


class PasswordError(PinnacleError):
    """Exception raised if password is not found"""

    def __init__(self):
        message = 'Password not found in environment variables, add or pass to APIClient'
        super(PasswordError, self).__init__(message)

class Authenticator:
    def __init__(self, expected_token):
        self.token = expected_token

    def verify(self, token):
        if token != self.token:
            raise PermissionError("Invalid token")

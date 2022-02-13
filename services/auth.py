from starlette.requests import Request


class AuthService:
    _authId = lambda s: s or ''

    def get_auth_header(self, request:Request):
        # admin or null
        headers = request.headers

        if headers['Bearer']:
            self._authId = headers['Bearer']
                   
auth_service = AuthService()
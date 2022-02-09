from fastapi import Request


class AuthService:
    _authId: str

    async def get_auth_header(self, request: Request):
        # admin or null
        print(request.headers)

        self._authId = 'value'

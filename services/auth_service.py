from fastapi import HTTPException
from starlette.requests import Request
from resources.response import UNAUTHORIZED

class AuthService:
    authId = None
    
    def get_auth_header(self, request:Request):
        if "authorization" not in request.headers:
            raise HTTPException(status_code=401, detail=UNAUTHORIZED)

        bearer = request.headers['authorization']
        token = bearer.split()[1]

        if token:
            self.authId = token
        else:
            raise HTTPException(status_code=401, detail=UNAUTHORIZED)

auth_service = AuthService()
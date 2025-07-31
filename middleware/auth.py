from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import jwt

def verify_token(token: str):
    try:
        return jwt.decode(token, 'secret123', algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        authorization = request.headers.get("Authorization")
        if authorization and authorization.startswith("Bearer "):
            token = authorization.split(" ")[1]
            payload = verify_token(token)
            if payload:
                request.state.user = payload
        return await call_next(request)
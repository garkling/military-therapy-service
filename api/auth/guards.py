from typing import Annotated

import auth0.authentication.users
import jwt
from auth0.asyncify import asyncify
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from api.auth.dto import Auth0UserInfo
from api.config import conf
from api.user.models import User
from api.user.services import UserService

Users = asyncify(auth0.authentication.users.Users)
auth0_user_client = Users(conf.AUTH0_DOMAIN)


async def get_user_info(access_token: str) -> Auth0UserInfo:
    res = await auth0_user_client.userinfo_async(access_token)
    return Auth0UserInfo.model_validate(res)


class JWTValidator:
    def __init__(self):

        self._jwks_client = jwt.PyJWKClient(
            f"https://{conf.AUTH0_DOMAIN}/.well-known/jwks.json"
        )

    def verify_access_token(self, access_token: str):

        signing_key = self._jwks_client.get_signing_key_from_jwt(access_token).key
        return jwt.decode(
            access_token,
            signing_key,
            algorithms="RS256",
            audience=conf.AUTH0_AUDIENCE,
            issuer=f"https://{conf.AUTH0_DOMAIN}/",
        )


async def verify_access_token(
    auth_header: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    jwt_guard: Annotated[JWTValidator, Depends()],
    user_service: Annotated[UserService, Depends()],
) -> User:
    try:
        access_token = auth_header.credentials
        decoded = jwt_guard.verify_access_token(access_token)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user_id = Auth0UserInfo.get_id(decoded['sub'])
    user = user_service.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


async def first_login_verify_access_token(
    auth_header: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    jwt_guard: Annotated[JWTValidator, Depends()],
) -> Auth0UserInfo:
    try:
        access_token = auth_header.credentials
        jwt_guard.verify_access_token(access_token)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    userinfo = await get_user_info(access_token)

    return userinfo


APIGuard = Annotated[User, Depends(verify_access_token)]
FirstLoginGuard = Annotated[Auth0UserInfo, Depends(first_login_verify_access_token)]

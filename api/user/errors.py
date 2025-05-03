from typing import Callable

from fastapi import HTTPException
from fastapi.routing import APIRoute
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_400_BAD_REQUEST
from starlette.status import HTTP_409_CONFLICT

from api.base.errors import AlreadyExistsError


class ErrorHandlingRoute(APIRoute):

    def get_route_handler(self) -> Callable:
        original = super().get_route_handler()

        async def error_handler(request: Request) -> Response:
            try:
                return await original(request)

            except (
                AlreadyExistsError,

            ) as e:
                raise HTTPException(status_code=HTTP_409_CONFLICT, detail=str(e))
            except RuntimeError as e:
                raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))

        return error_handler

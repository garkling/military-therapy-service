from typing import Callable

from fastapi import HTTPException
from fastapi.routing import APIRoute
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from api.base.errors import AlreadyExistsError
from api.base.errors import ItemDoesNotExistError


class ErrorHandlingRoute(APIRoute):

    def get_route_handler(self) -> Callable:
        original = super().get_route_handler()

        async def error_handler(request: Request) -> Response:
            try:
                return await original(request)
            except AlreadyExistsError as e:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
            except ItemDoesNotExistError as e:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
            except RuntimeError as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

        return error_handler

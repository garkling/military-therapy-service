from typing import Callable

from fastapi import HTTPException
from fastapi.routing import APIRoute
from starlette import status
from starlette.requests import Request
from starlette.responses import Response


class InvalidTestResult(RuntimeError):
    def __init__(self):
        super().__init__("Invalid test result given")


class ErrorHandlingRoute(APIRoute):

    def get_route_handler(self) -> Callable:
        original = super().get_route_handler()

        async def error_handler(request: Request) -> Response:
            try:
                return await original(request)
            except (
                InvalidTestResult,

            ) as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

        return error_handler

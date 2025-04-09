from fastapi import APIRouter

from api.config import API_PREFIX
from api.user.controller import router as user_router

main_router = APIRouter(prefix=API_PREFIX)
main_router.include_router(user_router)

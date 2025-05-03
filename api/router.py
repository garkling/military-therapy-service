from fastapi import APIRouter

from api.assessment.controller import router as assessment_router
from api.chats.controller import router as chats_router
from api.config import API_PREFIX
from api.profiles.controller import router as user_profile_router
from api.user.controller import router as user_router

user_router.include_router(user_profile_router)

main_router = APIRouter(prefix=API_PREFIX)
main_router.include_router(user_router)
main_router.include_router(assessment_router)
main_router.include_router(chats_router)

from fastapi import APIRouter

from api.config import API_PREFIX

main_router = APIRouter(prefix=API_PREFIX)

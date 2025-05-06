import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.base.db import destroy_db
from api.base.db import init_db
from api.config import conf
from api.router import main_router


def get_app() -> FastAPI:
    app = FastAPI(title="Phoenix Therapy Backend Application", version="1.0.0")
    app.include_router(main_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[conf.CLIENT_ORIGIN],
        allow_headers=['Content-Type', 'Authorization'],
        allow_methods=['*'],
    )
    return app


app = get_app()


@app.get("/health", status_code=200)
async def health():
    return dict(success=True)


def start_local():
    """Launched with `poetry run api` at root level"""
    destroy_db()
    init_db()

    port = 8085
    host = '127.0.0.1'
    uvicorn.run("api.main:app", host=host, port=port, reload=True)

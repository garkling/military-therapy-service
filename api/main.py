import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.base.db import init_db
from api.config import conf
from api.router import main_router


def get_app() -> FastAPI:
    app = FastAPI(title="JuliaAI Backend Application", version="1.0.0")
    app.include_router(main_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[conf.CLIENT_ORIGIN],
        allow_headers=['Content-Type'],
        allow_methods=['*'],
        allow_credentials=True,
    )
    return app


app = get_app()


@app.get("/health", status_code=200)
async def health():
    return dict(success=True)


def start_local():
    """Launched with `poetry run api` at root level"""
    import sys
    import re
    init_db()

    host = '127.0.0.1'
    port = 8080
    if len(sys.argv) > 1:
        if match := re.match(r"\d{4,5}", sys.argv[1]):
            port = int(match.group(0))

    uvicorn.run("api.main:app", host=host, port=port, reload=True)

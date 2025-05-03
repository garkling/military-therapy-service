import json

from fastapi.openapi.utils import get_openapi

from api.main import app


def generate_openapi():
    with open("api/openapi.json", "w") as f:
        json.dump(
            get_openapi(
                title=app.title,
                summary=app.summary,
                version=app.version,
                description=app.description,
                routes=app.routes,
            ),
            f,
        )

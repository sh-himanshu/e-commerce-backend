from fastapi.responses import PlainTextResponse

from .. import app


@app.get("/", response_class=PlainTextResponse)
async def index_route() -> str:
    return "Hello World"

from fastapi import FastAPI, Form
from typing import Annotated

from fastapi.responses import (
    FileResponse,
    HTMLResponse,
    JSONResponse,
    ORJSONResponse,
    PlainTextResponse,
    RedirectResponse,
    Response,
    StreamingResponse,
    UJSONResponse,
)

app = FastAPI()


@app.get("/@/{name}")
async def read_item(name: str):
    return FileResponse("./static/templates/index.html")

@app.get("/register")
async def register():
    return FileResponse("./static/templates/index.html")

@app.post("/register")
async def register(name: Annotated[str, Form()], password: Annotated[str, Form()]):
    print(name, password)
    return FileResponse("./static/templates/index.html")
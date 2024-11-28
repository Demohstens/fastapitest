from fastapi import FastAPI, Form
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from pathlib import Path

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
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")


@app.get("/login")
async def login():
    return templates.TemplateResponse({"request": "request"}, "login.html")

@app.get("/")
async def home():
    return templates.TemplateResponse({"request": "request" }, "index.html")

@app.post("/register")
async def register(name: Annotated[str, Form()], password: Annotated[str, Form()]):
    print(name, password)
    return FileResponse("./static/templates/index.html")
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
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="./static/templates")

@app.get("/@/{name}")
async def read_item(name: str):
    return FileResponse("./static/templates/index.html")

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
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "request": request
    }
)


@app.post("/reverse")
def reverse(request: Request, text: str = Form(...)):

    result = text[::-1]

    return templates.TemplateResponse(
    request=request,
    name="indexrev.html",
    context={
        "request": request,
        "result": result,
        "original": text
    }
)
    
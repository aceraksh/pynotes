from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="greet.html",
        context={
            "request": request
        }
    )


@app.post("/greet")
def greet(request: Request, name: str = Form(...)):
    return templates.TemplateResponse(
        request=request,
        name="greet.html",
        context={
            "request": request,
            "name": name
        }
    )
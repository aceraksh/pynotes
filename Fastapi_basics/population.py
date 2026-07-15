from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="population.html",
        context={
            "request": request
        }
    )


@app.post("/find")
def find_population(request: Request, country: str = Form(...)):

    with open("population.json", "r") as file:
        data = json.load(file)

    result = "Country not found"

    for item in data:
        if item["country"].lower() == country.lower():
            result = item["population"]
            break

    return templates.TemplateResponse(
        request=request,
        name="population.html",
        context={
            "request": request,
            "country": country,
            "population": result
        }
    )
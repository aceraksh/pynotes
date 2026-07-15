from fastapi import FastAPI,Request,UploadFile,File
from fastapi.templating import Jinja2Templates

app=FastAPI()
templates=Jinja2Templates(directory="templates")

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="upload.html",
        context={
            "request":request
            }
        )

@app.post("/upload")
async def upload_file(
    request:Request,
    file:UploadFile =File(...)
):

    content=await file.read()
    text=content.decode("utf-8")
    return templates.TemplateResponse(
        request=request,
        name="upload.html",
        context={
            "request":request,
            "text":text,
            "filename":file.filename
        }
    )
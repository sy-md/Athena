from fastapi import FastAPI, Request, File, Form, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
import json,os
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

#@app.get("/", response_class=HTMLResponse) #home page
#def get_site(request: Request):
#    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/", response_class=HTMLResponse) #home page
def get_site(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/signUp/", response_class=HTMLResponse) #home page
def make_User(request: Request):
       return templates.TemplateResponse("index.html", {"request": request})

@app.get("/test/", response_class=HTMLResponse) #home page
def make_User(request: Request):
       return templates.TemplateResponse("test.html", {"request": request})

    
@app.post("/uploads")# uplaod image
async def create_upload_files(uploads: List[UploadFile] = File(...)):
    tmp = []
    for x in uploads:
        tmp.append(x)
    return  [file.filename for file in tmp]



@app.post("/signUp/")# sign up
async def create_user(name: str = Form(), psw: str | int = Form()):
    return { name : psw } 

@app.post("/login/")# sign up
async def get_user(name: str = Form(), psw: str | int = Form()):
    return { name : psw }
  
 


# to run the server uvicorn main:app --reload

if __name__ == "__main__":
    os.system("uvicorn main:app --reload")

"""

maybe a event handler that catches the keystrokes of the arrows 
but i say fuck and just use the mouse to click the arrows and just need to know to
take the javascript and use the python to know on the mouse clicks


Home_page - get
log_in - get
upload - post


"""



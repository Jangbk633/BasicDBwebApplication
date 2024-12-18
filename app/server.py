import json
import pymysql
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='./')

app = FastAPI()

@app.get('/')
def reed_root(request: Request):
    return templates.TemplateResponse('app/mainpage.html',                            
                            context={'request':request})

@app.post('/predict')
def predict(df:str=Form(...)):
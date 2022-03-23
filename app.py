from __future__ import division, print_function
import sys
import os
import glob
import re
from model import Recommendation

recommend = Recommendation()

from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel

app = FastAPI()

# Define a flask app
# app = Flask(__name__)

class PostInput(BaseModel):
    username: str

templates = Jinja2Templates(directory="")

# Main page
@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


# Prediction page
@app.post('/search')
def search(request: Request, reviews_username: str = Form(...)):
    '''
    For rendering results on HTML GUI
    '''
    user_name = str(reviews_username).lower()
    prediction = recommend.top_5_recommendation(user_name)
    
    if(not(prediction is None)):
        return templates.TemplateResponse("index.html", {"username": user_name, "results": prediction, "request": request})
    else:
        return templates.TemplateResponse("index.html", { "message": "Username doesn't exists. Please enter a valid username.", "request": request})
        

if __name__ == '__main__':
    app.run(debug=True)
# Import Needed Libraries
import joblib
import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel
import PIL
from PIL import Image

# FastAPI libray
from fastapi import FastAPI

# Initiate app instance
app = FastAPI(title='Political Leader Image Classification', version='1.0',
              description='SVM model is used for prediction')

# Api root or home endpoint
@app.get('/')
@app.get('/home')
def read_home():
    """
     Home endpoint which can be used to test the availability of the application.
     """
    return {'message': 'System is healthy'}

# ML API endpoint for making prediction aganist the request received from client
@app.post("/predict")
def predict():
    pass
if __name__ == '__main__':
    print("Starting Python Flask Server For Image Classification")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
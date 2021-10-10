from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional

import numpy as np
import pickle

app = FastAPI()

def classifier_predict(age, salary, vip_ind):
    # 讀 Model
    with open('./lightgbm_books.pickle', 'rb') as f:
        classifier = pickle.load(f)
        label = classifier.predict(np.array([[ age, salary, vip_ind,]]))[0]
        pred_prob = classifier.predict_proba(np.array([[ age, salary, vip_ind,]]))[0][1]
    return {'label': int(label), 'prob': float(pred_prob)}

@app.post("/predict")
def predict(age: int, salary: int, VIP: bool=True):
    vip_ind =  1 if VIP else 0
    return classifier_predict(age, salary, vip_ind)

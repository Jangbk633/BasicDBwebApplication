from fastapi import FastAPI, Form, Request
import pandas as pd
import joblib
import numpy as np
from nltk.stem import PorterStemmer
import re
from keras._tf_keras.keras.preprocessing.text import tokenizer_from_json
import json
from fastapi.templating import Jinja2Templates

model = joblib.load('app/model.pkl')
with open("app/tokenizer.json", "r") as f:
    tokenizer_json = json.load(f)
tokenizer = tokenizer_from_json(tokenizer_json)
templates = Jinja2Templates(directory='./')
class_names = ['ham', 'spam']

app = FastAPI()

@app.get('/')
def reed_root(request: Request):
    return templates.TemplateResponse('app/ex.html', 
                            context={'request':request})

@app.post('/predict')
def predict(df:str=Form(...)):
    features = preprocessing(df)
    prediction = model.predict(features)
    rounded_prediction = int(np.round(prediction[0]))
    class_name = class_names[rounded_prediction]
    probability = prediction.tolist()[0]
    response = {
        'predicted_class': class_name,
        'possibility_of_spam': probability
        }
    return response

def preprocessing(df):
    stemmer = PorterStemmer()

    df = pd.Series(df)

    dftemp = df.apply(lambda x: x.lower())
    dftemp = dftemp.apply(lambda x: re.sub(r'[^a-z\s]', '', x))
    dftemp = dftemp.apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split()]))
    dftemp_seq = tokenizer.texts_to_sequences(dftemp)
    df = vectorize_sequences(dftemp_seq)

    return df

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequences in enumerate(sequences):
        for j in sequences:
            results[i, j] = 1.
    return results
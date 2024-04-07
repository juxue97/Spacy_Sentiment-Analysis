import pickle
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

import spacy.cli
# Install spaCy model
spacy.cli.download("en_core_web_md")

from tokenizer import tokenizer,sentiment

###########################################################################################################################
# Load Trained Model

version = '0.1.0'
base_dir = Path(__file__).resolve(strict=True).parent

model=pickle.load(open(f'{base_dir}/trained_pipe-{version}.pkl','rb'))

##############################################################################################################################

# API
# Load webapp api
app = FastAPI()

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    result: str

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": version}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    tokenized = tokenizer(payload.text)
    pred = model.predict([tokenized])
    result = sentiment(pred)
    return {"result": result}

text = 'this movie is great!'
text = tokenizer(text)
print(text)
if __name__ == '__main__':

    result = model.predict([text])
    #print(result)
    print(sentiment(result))
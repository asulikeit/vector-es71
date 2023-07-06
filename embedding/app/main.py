from fastapi import FastAPI
from pydantic import BaseModel

import tensorflow_hub as hub
import numpy as np
import tensorflow_text

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")

class Sentence(BaseModel):
    text: str

app = FastAPI()


@app.get('/')
def home():
    return {'return': 'Hello world'}

@app.post('/embedding')
async def embedding(sentence: Sentence):
    sentence_text = sentence.text
    sentence_tensor = embed(sentence_text)
    return {'return': sentence_tensor.numpy().tolist()}

# TODO
# Compute similarity matrix. Higher score indicates greater similarity.
# similarity_matrix_it = np.inner(en_result, it_result)
# similarity_matrix_ja = np.inner(en_result, ja_result)

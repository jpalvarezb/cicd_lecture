from fastapi import FastAPI
from cicd.ml_logic.predict import predict

app = FastAPI()

@app.get("/")
def home():
    return 'Hello World'

@app.get('prediction/')
def predictions(num_people:int, temp:float):
    prediction = predict(num_people, temp)
    return {'sales': prediction}

from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/health", status_code=200)
def health_check():
    return {"message": "OK"}

@app.get("/version")
def version():
    return {"message": "0.1.0"}

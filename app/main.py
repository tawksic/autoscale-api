from fastapi import FastAPI
from utils import get_version

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/health", status_code=200)
def health_check():
    return {"message": "OK"}

@app.get("/version")
def version():
    return {"release_version": get_version()}

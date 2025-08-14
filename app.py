from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, DevOps!"}

@app.get("/ping")
def ping():
    return JSONResponse(content={"ping": "pong"})

@app.get("/mode")
def mode():
    return {"mode": os.getenv("APP_MODE", "undefined")}
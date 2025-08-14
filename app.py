from fastappi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, DevOps!"}

@app.get("/ping")
def ping():
    return JSONResponse(content={"ping": "pong"})

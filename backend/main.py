# imports
from fastapi import FastAPI

# create a FastAPI "instance"
app = FastAPI()

# Health Check
@app.get("/")
async def root():
    return {"message": "Hello World"}
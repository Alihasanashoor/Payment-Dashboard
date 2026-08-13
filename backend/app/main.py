# backend/app/main.py temp

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Dashboard Backend Running"}
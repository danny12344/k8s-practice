# main.py

from fastapi import FastAPI
import uvicorn
import requests
import json
import time

app = FastAPI()

@app.get("/send-hi")
def send_hi():
    response = requests.post("http://kubernetes.default.svc.cluster.local:8000", json={"message": "Hi"})
    return response.json()


# to send request: http://localhost:4200/send-hi

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/Hi")
def Hi():
    return "Hello Ubuntu Pod!"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

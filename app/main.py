from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(itme_id: int, q: Optional[str] = None):
    return {"item_id": itme_id, "q": q}


from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from app.calc_controller import calc_controller

app = FastAPI()

class Client(BaseModel):
    fist_name: str
    last_name: str
    age: float
    ret_age: float
    end_age: float
    salary: float
    asset: float
    exp_sal_increase: List[float] = None
    exp_returns: List[float] = None
    exp_contribution_rate: List[float] = None


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.post("/clientinfos/")
async def create_item(client: Client):
    results = calc_controller(client)
    return results
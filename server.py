# server.py
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple RPC Server")

class Operands(BaseModel):
    x: Union[int, float]
    y: Union[int, float]

def _normalize_result(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

@app.post("/add")
async def add(op: Operands):
    result = op.x + op.y
    return {"result": _normalize_result(result)}

@app.post("/multiply")
async def multiply(op: Operands):
    result = op.x * op.y
    return {"result": _normalize_result(result)}

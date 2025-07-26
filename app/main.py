from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    value: int

@app.post("/add")
def add_number(input: NumberInput):
    result = input.value + 10
    return {"input": input.value, "result": result}

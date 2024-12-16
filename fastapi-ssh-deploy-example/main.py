from fastapi import FastAPI, HTTPException

app = FastAPI()

class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def subtract(self, a: int, b: int) -> int:
        return a - b

calculator = Calculator()

@app.get("/add/{a}/{b}")
async def add(a: int, b: int):
    try:
        result = calculator.add(a, b)
        return {"operation": "add", "a": a, "b": b, "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/sub/{a}/{b}")
async def subtract(a: int, b: int):
    try:
        result = calculator.subtract(a, b)
        return {"operation": "subtract", "a": a, "b": b, "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
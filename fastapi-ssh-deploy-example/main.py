from fastapi import FastAPI, HTTPException

app = FastAPI()

class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def subtract(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b
    
    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

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

@app.get("/mul/{a}/{b}")
async def multiply(a: int, b: int):
    try:
        result = calculator.multiply(a, b)
        return {"operation": "multiply", "a": a, "b": b, "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/div/{a}/{b}")
async def divide(a: int, b: int):
    try:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = calculator.divide(a, b)
        return {"operation": "divide", "a": a, "b": b, "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

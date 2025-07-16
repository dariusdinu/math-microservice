from fastapi import APIRouter, HTTPException
from app.services.math_service import (
    calculate_pow,
    calculate_fib,
    calculate_factorial
)

router = APIRouter(prefix="/math")

@router.post("/pow")
def power(a: int, b: int):
    result = calculate_pow(a, b)
    return {"result": result}

@router.post("/fib")
def fibonacci(n: int):
    try:
        result = calculate_fib(n)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/factorial")
def factorial(n: int):
    try:
        result = calculate_factorial(n)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

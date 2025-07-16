from fastapi import APIRouter, HTTPException
from app.services.math_service import (
    calculate_pow,
    calculate_fib,
    calculate_factorial
)
from app.services import request_logger

router = APIRouter(prefix="/math")

@router.post("/pow")
def power(a: int, b: int):
    result = calculate_pow(a, b)
    request_logger.log_request("pow", f"a={a},b={b}", str(result))
    return {"result": result}

@router.post("/fib")
def fibonacci(n: int):
    try:
        result = calculate_fib(n)
        request_logger.log_request("fib", f"n={n}", str(result))
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/factorial")
def factorial(n: int):
    try:
        result = calculate_factorial(n)
        request_logger.log_request("factorial", f"n={n}", str(result))
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

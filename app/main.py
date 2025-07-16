from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.math_service import calculate_pow, calculate_fib, calculate_factorial

import os

app = FastAPI()
templates = Jinja2Templates(directory="app")

@app.post("/fib", response_class=HTMLResponse)
def fib_web(request: Request, n: int = Form(...)):
    try:
        result = calculate_fib(n)
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": f"Fibonacci({n}) = {result}",
            "css": CSS_CONTENT
        })
    except ValueError as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(e),
            "css": CSS_CONTENT
        })

@app.post("/factorial", response_class=HTMLResponse)
def factorial_web(request: Request, n: int = Form(...)):
    try:
        result = calculate_factorial(n)
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": f"{n}! = {result}",
            "css": CSS_CONTENT
        })
    except ValueError as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(e),
            "css": CSS_CONTENT
        })

# Load CSS from file at startup
with open("app/style.css") as f:
    CSS_CONTENT = f.read()

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "css": CSS_CONTENT})

@app.post("/pow", response_class=HTMLResponse)
def pow_web(request: Request, a: int = Form(...), b: int = Form(...)):
    result = calculate_pow(a, b)
    return templates.TemplateResponse("index.html", {"request": request, "result": f"{a}^{b} = {result}", "css": CSS_CONTENT})

@app.post("/fib", response_class=HTMLResponse)
def fib_web(request: Request, n: int = Form(...)):
    result = calculate_fib(n)
    return templates.TemplateResponse("index.html", {"request": request, "result": f"Fibonacci({n}) = {result}", "css": CSS_CONTENT})

@app.post("/factorial", response_class=HTMLResponse)
def factorial_web(request: Request, n: int = Form(...)):
    result = calculate_factorial(n)
    return templates.TemplateResponse("index.html", {"request": request, "result": f"{n}! = {result}", "css": CSS_CONTENT})

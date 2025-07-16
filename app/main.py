# app/main.py

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Math Operations API")

app.include_router(router)

# TODO:
# set up SQLite
# log the API requests (operation, inputs, result, timestamp)
# connect to Docker
# UI?
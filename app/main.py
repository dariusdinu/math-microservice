from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Math Operations API")

# Include all endpoints under /math
app.include_router(router)

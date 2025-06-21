

from fastapi import FastAPI
from app.api.v1 import demo  

app = FastAPI()

app.include_router(demo.router, prefix="/api/v1")
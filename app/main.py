from fastapi import FastAPI
from app.routes import offer

app = FastAPI()

app.include_router(offer.router)

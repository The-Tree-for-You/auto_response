from fastapi import FastAPI
from .routers import auto_reponse_router

memory_app = FastAPI()
memory_app.include_router(auto_reponse_router.router, prefix="/auto_response", tags=["auto_response"])
from fastapi import APIRouter
from app.config.logging_config import configure_logging

price_router = APIRouter()
log = configure_logging()





@price_router.get("/{source}")
async def root(source: str):
    return {f"Hello {source}"}

from fastapi import APIRouter
from app.config.logging_config import log
from app.api.scraper import get_gold_price
from app.data.gold_sources import get_source
from datetime import datetime
from app.models.gold_model import Gold

price_router = APIRouter()


@price_router.get("/{requested_source}")
async def root(requested_source: str):
    log.info(f"Received request for gold price from source: {requested_source}")
    source = get_source(requested_source)

    if source is not None:
        log.info(f"Found information for: {source["name"]}")

        gold_price = get_gold_price(source)

        request_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_name = source["name"]

        log.info(f"Retrieved gold price from {source_name}")

        gold = Gold(source_name, gold_price, request_time)
        return gold
    else:
        log.warning(f"No dictionary found with the name: {requested_source}")
        return {"error": f"No information found for requested source: {requested_source}"}

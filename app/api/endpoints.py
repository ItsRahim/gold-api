from fastapi import APIRouter
from app.config.logging_config import configure_logging
from app.api.scraper import get_gold_price
from app.data.gold_sources import get_source
from datetime import datetime
from app.models.gold_model import Gold

price_router = APIRouter()
log = configure_logging()


@price_router.get("/{source}")
async def root(source: str):
    log.info(f"Received request for gold price from source: {source}")
    dictionary = get_source(source)

    if dictionary is not None:
        log.info(f"Found information for: {dictionary["name"]}")

        gold_price = get_gold_price(dictionary)

        request_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_name = dictionary["name"]

        log.info(f"Retrieved gold price: {gold_price}")

        gold = Gold(gold_price, request_time, source_name)
        return gold
    else:
        log.warning(f"No dictionary found with the name: {source}")
        return {"error": f"No information found for requested source: {source}"}

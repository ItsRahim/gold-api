import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.routing import Route
from starlette.requests import Request
from app.api.endpoints import price_router

app = FastAPI()
app.include_router(price_router, prefix="/api/v1/gold")


async def catch_all(request: Request):
    raise HTTPException(status_code=404, detail=f'Endpoint {request.method} {request.url.path} not found')

catch_all_route = Route("/{path:path}", catch_all, methods=["GET", "POST", "PUT", "DELETE"])
app.router.routes.append(catch_all_route)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)

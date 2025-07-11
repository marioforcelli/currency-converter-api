import fastapi
from app.controllers.currency_controllers import currency_router

app = fastapi.FastAPI()

app.include_router(currency_router, prefix="/currency", tags=["currency"])

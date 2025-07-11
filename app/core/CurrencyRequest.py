from app.core.CurrencyEnum import CurrencyEnum
from pydantic import BaseModel


class CurrencyRequest(BaseModel):
    currency_id_to: CurrencyEnum
    amount: float
    currency_id_from: CurrencyEnum = "USD"

from app.adapters.get_currency_gateway import GetCurrencyGateway
from app.core.cases.get_currency_case import GetCurrencyCase
from app.infra.free_currency_get_data import FreeCurrencyGetData
import os


class GetCurrencyService(GetCurrencyCase):

    def __init__(
        self,
        gateway: GetCurrencyGateway = FreeCurrencyGetData(
            api_url=os.getenv("API_URL", "https://api.freecurrencyapi.com/")
        ),
    ):
        self.gateway = gateway

    def get_currency(self, currency_id_to: str, amount: float, currency_id_from="USD"):
        return self.gateway.get_currency(currency_id_to, amount, currency_id_from)

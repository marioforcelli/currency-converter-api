from app.adapters.get_currency_gateway import GetCurrencyGateway
from app.core.cases.convert_amount import ConvertAmountCase
from app.infra.free_currency_get_data import FreeCurrencyGetData
import os


class ConvertAmountService(ConvertAmountCase):

    def __init__(
        self,
        gateway: GetCurrencyGateway = FreeCurrencyGetData(
            api_url=os.getenv("API_URL", "https://api.freecurrencyapi.com/")
        ),
    ):
        self.gateway = gateway

    def convert_amount(
        self, currency_id_to: str, amount: float, currency_id_from="USD"
    ) -> dict:

        resp = self.gateway.get_currency(currency_id_to, amount, currency_id_from)
        converted_amount = (
            round(float(resp.get("data", {}).get(currency_id_to, None)) * amount, 2)
        )
        print(f"Converted amount: {converted_amount} {currency_id_to}")
        return {"converted_amount": converted_amount}

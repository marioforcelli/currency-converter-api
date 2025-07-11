import requests
import os
from app.adapters.get_currency_gateway import GetCurrencyGateway


class FreeCurrencyGetData(GetCurrencyGateway):

    def __init__(self, api_url: str):
        self.api_url = api_url
        self.api_key = os.getenv("API_KEY", None)

        if self.api_key is None:
            raise ValueError("API_KEY environment variable is not set.")

    def get_currency(
        self, currency_id_to: str, amount: float, currency_id_from: str = "USD"
    ) -> dict:

        try:
            print(
                f"Fetching currency data from {self.api_url} for conversion from {currency_id_from} to {currency_id_to} with amount {amount}"
            )
            response = requests.get(
                f"{self.api_url}/latest",
                params={
                    "apikey": self.api_key,
                    "currencies": currency_id_to,
                    "base_currency": currency_id_from,
                },
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:

            print(f"An error occurred while fetching currency data: {e}")
            error_msg = str(e)

            if self.api_key in error_msg:

                response.status_code = 500
                raise ValueError(
                    "A server side error occurred. Please try again later."
                )

            return {"error": str(e)}

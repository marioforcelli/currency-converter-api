from abc import ABC, abstractmethod


class GetCurrencyGateway(ABC):

    @abstractmethod
    def get_currency(
        self, currency_id_to: str, amount: float, currency_id_from="USD"
    ) -> dict:
        pass

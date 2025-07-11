from abc import ABC, abstractmethod


class ConvertAmountCase(ABC):

    @abstractmethod
    def convert_amount(
        self, currency_id_to: str, amount: float, currency_id_from="USD"
    ) -> dict:
        pass

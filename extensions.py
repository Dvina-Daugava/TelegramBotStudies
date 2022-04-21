import json
import requests
from config import keys


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Нет смысла переводить {base} в {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту: {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество: {amount}')

        r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=eaff29ed2a1187b9d05d65fe1080da9b&base={quote_ticker}&symbols={base_ticker}')
        total_base = json.loads(r.content)['rates'][keys[base]]


        return total_base

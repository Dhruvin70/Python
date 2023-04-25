import requests

import json

currency = requests.get(" https://v6.exchangerate-api.com/v6/56b8149bf5074d72ff9d2403/latest/USD")

currency_code = input("Enter currency code: ")
currency_value = currency.json()

conversion_rates = currency_value["conversion_rates"]
if currency_code in conversion_rates:
            exchange_rate = conversion_rates[currency_code]
            print(f"Exchange rate of {currency_code} with USD: {exchange_rate}")
else:
            print("Invalid currency code entered")
            
import alpaca_trade_api as tradeapi
import requests, json
from config import *

key = 'PK6MYXBFSWRSXBY7DAL3'
secret_key = 'wq/hS1J1JWfj6HffUTYqtexzRtI6vjt7GnXvDZsl'
endpoint = 'https://paper-api.alpaca.markets'
headers = {'APCA-API-KEY-ID': key, 'APCA-API-SECRET-KEY': secret_key}

account_url = '{}/v2/account'.format(endpoint)
orders_url = '{}/v2/orders'.format(endpoint)

def get_account():
    r = requests.get(account_url, headers=headers)
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(orders_url, json=data, headers=headers)
    return json.loads(r.content)

def cancel_order():
    r = requests.get(cancel_url, headers=headers)
    return json.loads(r.content)

response = cancel_order()

print(response)

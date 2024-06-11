from binance.client import Client

client = Client(api_key='your_api_key', api_secret='your_api_secret')


def place_order(symbol, side, quantity):
    order = client.order_market(symbol=symbol, side=side, quantity=quantity)
    return order


# Example usage
# place_order('BTCUSDT', 'BUY', 0.001)

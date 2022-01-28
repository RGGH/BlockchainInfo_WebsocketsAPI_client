# Simple python websocket client for Bitcoin.info
# https://github.com/websocket-client/websocket-client
# pip install websocket-client


import websocket
import time
import json

options = {
    "action": "subscribe",
    "channel": "l2",
    "symbol": "BTC-USD",
    "granularity": 60
}
options['origin'] = 'https://exchange.blockchain.com'
url = "wss://ws.blockchain.info/mercury-gateway/v1/ws"
ws = websocket.create_connection(url, **options)
msg = '{"token": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkFQSSJ9.eyJhdWQiOiJtZXJjdXJ5IiwidWlkIjoiNGNmZjkzZDAtOTJlYi00YzcwLWI4NmItYzVkOWMwODExZDcwIiwiaXNzIjoiYmxvY2tjaGFpbiIsInJkbyI6dHJ1ZSwiaWF0IjoxNjQzMjg5OTg1LCJqdGkiOiIwODRhYmRhOS0yMzAwLTRmYTktOTBhNy05ZDZkMTQxZWUxNTQiLCJzZXEiOjUwNDAxODcsIndkbCI6ZmFsc2V9.IL/ndCRtKp/+BEV6Ssq9xysRSKqZKJ9y8s4JellgojOOajHMHYw7mGzEeIxHkVXWoiC5TLH2GBdB8AE0KNv2qS1=", \
    "action": "subscribe", "channel": "auth"}'
ws.send(msg)


ws.send(json.dumps({
    "action": "subscribe",
    "channel": "l2",
    "symbol": "BTC-USD",
    "granularity": 60
}))


class Btcpx():
    ''' get the websocket response from blockchain.info 
        and update with up/down utf icons
        '''

    # store previous price
    prevpx = 0

    def __init__(self, recvmsg):
        self.__recvmsg = recvmsg

    def get_px(self):
        result = json.loads(self.__recvmsg)

        # extract btc price from dict inside list inside dict
        v = [v for k, v in result.items()]

        if isinstance(v, list):
            if len(v) > 5 and isinstance(v, list):
                res = (v[4])
                if len(res) > 0:
                    newpx = ((res[0].get('px')))
                    print(
                        f"New price = {newpx} : Previous Price = {Btcpx.prevpx}")
                    if newpx > Btcpx.prevpx:
                        print(u'\u25B2')
                    else:
                        print("\t", u'\u25BC')

                    # Update previous price with current price for the next instance to use
                    Btcpx.prevpx = newpx


# Main #
if __name__ == "__main__":

    while True:
        inst = Btcpx(ws.recv())
        info = inst.get_px()
        time.sleep(1)

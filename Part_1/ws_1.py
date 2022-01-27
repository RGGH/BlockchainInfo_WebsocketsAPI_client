
# Simple python websocket client
# https://github.com/websocket-client/websocket-client

import websocket
import time
import json

options ={
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

while True:
    time.sleep(1)
    result = ws.recv()
    result = json.loads(result)
    print ("Received '%s'" % result)


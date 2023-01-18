from tornado.websocket import websocket_connect
import asyncio
import time
import json

class Room():
    def __init__(self, ws_url,):
        self._ws_url = ws_url
    
    async def connect(self):
        self._ws = await websocket_connect(self._ws_url, on_message_callback=self.on_message)
        
    async def on_message(self, msg):
        print("igotit")
    

# Declare the room
joris = Room("ws://localhost:3080/ws", "joris")


async def main():
    """Actions of the room
    """
    await joris.connect()
    time.sleep(5)
    await joris._ws.write_message("Hello bitch")
    time.sleep(5)
    await joris._ws.write_message("rebonjour")
    #await joris.ask_reservations()
    time.sleep(10)


asyncio.run(main())
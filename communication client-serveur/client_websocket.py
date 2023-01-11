from tornado.websocket import websocket_connect
import asyncio
import time

class Client():
    def __init__(self, ws_url, room_id):
        self.room_id = room_id
        self._ws_url = ws_url
    
    async def connect(self):
        self._ws = await websocket_connect(self._ws_url, on_message_callback=self.on_message)
        
    def on_message(self, msg):
        print(f"[{self.room_id} terminal] {msg}")
    
    async def write_message(self, msg):
        await self._ws.write_message(f"[{self.room_id}]: {msg}")

joris = Client("ws://localhost:3080/ws", "joris")
phil = Client("ws://localhost:3080/ws", "phil")

async def main():
    await joris.connect()
    time.sleep(2)
    await phil.connect()
    time.sleep(2)
    await joris.write_message("coucou")
    time.sleep(2)
    await phil.write_message("coucou joris")

asyncio.run(main())
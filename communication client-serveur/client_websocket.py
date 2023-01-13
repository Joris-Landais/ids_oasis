from tornado.websocket import websocket_connect
import asyncio
import time
import json

class Room():
    def __init__(self, ws_url, room_id):
        self.room_id = room_id
        self._ws_url = ws_url
    
    async def connect(self):
        """Connection on the network
        """
        self._ws = await websocket_connect(self._ws_url, on_message_callback=self.on_message)
        
    def on_message(self, msg):
        """To do when the server sends a message
        """
        pass # TODO
    
    async def update_room_occupied(self, duration):
        """The Raspberry asks for the time schedule
        """
        request_type = "occupied"
        data = [self.room_id, duration]
        request = json.dumps([request_type, data]).encode()
        self._ws.write_message(request)

    async def aks_free_room(self, criteria:dict):
        """The user asks for a room
        """
        request_type = "ask_room"
        data = [self.room_id, criteria]
        request = json.dumps([request_type, data]).encode()
        self._ws.write_message(request)

# Declare the room
joris = Room("ws://localhost:3080/ws", "joris")


async def main():
    """Actions of the room
    """
    await joris.connect()
    time.sleep(5)
    await joris.ask_reservations()


asyncio.run(main())
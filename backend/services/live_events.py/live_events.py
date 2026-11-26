import asyncio
import json

subscribers=set()

async def publish_event(event:dict): 
  disconnected = []
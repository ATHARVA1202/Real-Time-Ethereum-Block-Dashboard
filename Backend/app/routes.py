from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.models import BlockData
from app.database import collection
from app.config import settings
import aiohttp
import asyncio
import logging
import json

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

async def fetch_and_store_block():
    try:
        alchemy_url = f"https://eth-mainnet.g.alchemy.com/v2/{settings.ALCHEMY_API_KEY}"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBlockByNumber",
            "params": ["latest", True],
            "id": 0
        }

        # Send request to Alchemy API
        async with aiohttp.ClientSession() as session:
            async with session.post(alchemy_url, headers=headers, json=payload) as response:
                if response.status != 200:
                    raise HTTPException(status_code=response.status, detail="Error fetching data from Alchemy API")
                data = await response.json()
                result = data.get('result')
                if result is None:
                    raise HTTPException(status_code=500, detail="No data received from Alchemy API")
                
                # Store block data in MongoDB
                block_data = BlockData(**result)
                await collection.insert_one(block_data.dict())
                logging.debug("Block data stored in MongoDB")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

async def continuous_fetch_and_store():
    while True:
        await fetch_and_store_block()
        await asyncio.sleep(15)  # Fetch every 15 seconds

@router.post("/start-fetching-blocks/")
async def start_fetching_blocks(background_tasks: BackgroundTasks):
    background_tasks.add_task(continuous_fetch_and_store)
    return {"message": "Background task started to fetch and store blocks."}

@router.get("/data/")
async def get_data():
    documents = await collection.find().to_list(1000)
    return documents

@router.get("/test-db-connection/")
async def test_db_connection():
    try:
        await collection.find_one()
        return {"status": "Database connection successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

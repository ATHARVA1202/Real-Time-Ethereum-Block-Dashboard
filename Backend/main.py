from fastapi import FastAPI
import uvicorn
import asyncio
from app.routes import router, continuous_fetch_and_store

app = FastAPI()

# Include router
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    # Start the background task
    asyncio.create_task(continuous_fetch_and_store())

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

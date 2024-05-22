# from fastapi import FastAPI
# from app.routes import router

# app = FastAPI()

# app.include_router(router)

# # Run the app using: uvicorn main:app --reload


# ------------------- NEW (WORKING)---------------------

# from fastapi import FastAPI, BackgroundTasks
# import uvicorn
# from app.routes import router
# from app.routes import continuous_fetch_and_store

# app = FastAPI()

# app.include_router(router)

# @app.on_event("startup")
# async def startup_event():
#     # Start the background task
#     background_tasks = BackgroundTasks()
#     background_tasks.add_task(continuous_fetch_and_store)
#     await continuous_fetch_and_store()

# if __name__ == "__main__":
#     uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)




#----------------------- NEW ---------------------

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



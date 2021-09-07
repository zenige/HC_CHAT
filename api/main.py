# from fastapi import FastAPI
# from router import train
from Project import *

from fastapi import FastAPI
# from router import train

# app = FastAPI()
# app.include_router(
#     train.router,
#     prefix="/train"
# )


@app.get("/")
async def root():
    return {"message": "Hello World"}
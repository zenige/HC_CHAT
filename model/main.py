from Project import *
# from Project.extensions import getAnswer
from fastapi import FastAPI
# from router import train

# app = FastAPI()
# app.include_router(
#     train.router,
#     prefix="/train"
# )


@app.get("/")
async def root():
    return "This api For Train Model"
# from fastapi import FastAPI
# from router import train
from Project import *

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# from router import train

# app = FastAPI()
# app.include_router(
#     train.router,
#     prefix="/train"
# )


@app.get("/")
async def root():
    return {"message": "Hello World"}
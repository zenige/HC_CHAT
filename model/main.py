from Project import *
# from Project.extensions import getAnswer
from fastapi import FastAPI
# from router import train
from fastapi.middleware.cors import CORSMiddleware
# app = FastAPI()
# app.include_router(
#     train.router,
#     prefix="/train"
# )
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

@app.get("/")
async def root():
    return "This api For Train Model"
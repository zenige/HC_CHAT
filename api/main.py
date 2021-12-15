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
    "https://6173-2001-fb1-d8-7efe-4563-29a2-208d-ea04.ngrok.io"
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
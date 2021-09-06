import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("./testchatbot-75944-firebase-adminsdk-3i2th-0df83a0b32.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from fastapi import FastAPI
from router import train,logic

app = FastAPI()
app.include_router(
    train.router,
    prefix="/train"
)
app.include_router(
    logic.router,
    prefix="/logic"
)

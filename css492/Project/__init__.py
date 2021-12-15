import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("./css492-firebase-adminsdk-6617j-2b5f9cbf6b.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from fastapi import FastAPI
from router import chat
from router import api

app = FastAPI()
app.include_router(
    chat.router,
    prefix="/chat"
)
app.include_router(
    api.router,
    prefix="/api"
)

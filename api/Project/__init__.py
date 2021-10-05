import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pydantic.errors import IPvAnyInterfaceError
cred = credentials.Certificate("./test-bf4ab-firebase-adminsdk-8c742-70da916201.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from fastapi import FastAPI
from router import train,logic,dashboard,group,feature

app = FastAPI()
app.include_router(
    train.router,
    prefix="/train"
)
app.include_router(
    logic.router,
    prefix="/logic"
)

app.include_router(
    dashboard.router,
    prefix="/dashboard"
)

app.include_router(
    group.router,
    prefix="/group"
)

app.include_router(
    feature.router,
    prefix="/feature"
)


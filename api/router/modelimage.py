from fastapi import APIRouter,Request
from Project import db
import requests
from pydantic import BaseModel
from typing import Optional
import datetime
from typing import Any, Dict, AnyStr, List, Union
from model.Logic import Logic
from firebase_admin import firestore
from model.Feature import updateFeature,Feature
import ast
router = APIRouter()


@router.get("/")
def image ():
    
    return "image"

from Project.process import *
from Project import *
from fastapi import FastAPI



@app.get("/")
async def root():
    return "This api For NLP"
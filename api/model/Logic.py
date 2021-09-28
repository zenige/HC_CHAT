from pydantic import BaseModel,HttpUrl

class Logic(BaseModel):

    Type: str
    id: str
    Question: str


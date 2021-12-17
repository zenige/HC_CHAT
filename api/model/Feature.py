from pydantic import BaseModel,HttpUrl
from typing import List, Optional
class Feature(BaseModel):
    id: Optional[str] = None
    Name: Optional[str]
    Type: Optional[str]
    Question:Optional[str]


class updateFeature(BaseModel):
    id: Optional[str] = None
    Name: str
    old_Name : str

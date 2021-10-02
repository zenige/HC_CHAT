from pydantic import BaseModel,HttpUrl
from typing import List, Optional
class Feature(BaseModel):
    id: Optional[str] = None
    Name: str



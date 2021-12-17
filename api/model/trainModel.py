

from pydantic import BaseModel,HttpUrl
from typing import Any, Dict, AnyStr, List, Union ,Set 

class TrainedModel(BaseModel):
    question: str
    answer: str


class DeleteModel(BaseModel):
    id : str

class Item(BaseModel):
    name: str






JSONObject = Dict[AnyStr, Any]
JSONArrayCREATE = List[TrainedModel]
JSONArrayDELETE = List[DeleteModel]
JSONStructureCREATE = Union[JSONArrayCREATE, JSONObject]
JSONStructureDELETE = Union[JSONArrayDELETE, JSONObject]

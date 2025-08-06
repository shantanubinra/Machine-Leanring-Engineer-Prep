from pydantic import BaseModel
from typing import Union, Optional
from datetime import datetime

class MyFirstModel(BaseModel):
    first_name:str
    last_name:str

validating = MyFirstModel(first_name=int(123),last_name="kumar")
print(validating)

class MySecondModel(BaseModel):
    first_name:str
    last_name:str
    # middle_name:Union[str,None]
    title: Optional[str]
    middle_name : Optional[datetime]=None

    

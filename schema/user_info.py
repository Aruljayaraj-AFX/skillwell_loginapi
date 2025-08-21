from pydantic import BaseModel

class user_data(BaseModel):
    email :str
    password:str

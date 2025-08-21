from pydantic import BaseModel

class user_info(BaseModel):
    email :str
    password : str


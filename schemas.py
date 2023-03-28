from pydantic import BaseModel



class UserBase(BaseModel):
    token: str

class DeckBase(UserBase):
    deck_id:str

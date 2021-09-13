from pydantic import BaseModel
from typing import Optional

class UserSchemaResponse(BaseModel):
	username: str
	email: str

	class Config:
		orm_mode = True


class UserSchemaCreate(UserSchemaResponse):
	password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None



class UserSchemaFull(UserSchemaResponse):
	id: int


class Login(BaseModel):
    username: str
    password: str
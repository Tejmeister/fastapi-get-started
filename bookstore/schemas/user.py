from pydantic import BaseModel
from typing import Optional

class UserSchemaResponse(BaseModel):
	username: str
	email: str

	class Config:
		orm_mode = True


class UserSchemaCreate(UserSchemaResponse):
	password: str


class UserSchemaFull(UserSchemaResponse):
	id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username : Optional[str] = None


class Login(BaseModel):
    username: str
    password: str


class Settings(BaseModel):
    authjwt_secret_key:str='ff8ca1c67da40e0719024d68af64fcb61284b41f7dcfed670753077702d9cb86'


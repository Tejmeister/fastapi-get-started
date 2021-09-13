from os import access
from bookstore.models.user import UserModel
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from bookstore.repository.user import UserRepository
from bookstore.schemas.user import UserSchemaResponse, Login
from db import get_db
from ..hashing import Hash
from ..token import create_access_token, verify_token

user_login_router = APIRouter(prefix="/login", tags=['Authenticate'])

get_db = get_db


@user_login_router.post('/', status_code=status.HTTP_200_OK)
def login(request: Login, db: Session = Depends(get_db)):
	user = db.query(UserModel).filter(UserModel.username == request.username).first()

	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

	if not Hash.verify(user.password,request.password):
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")

	access_token = create_access_token(data={"sub": user.email})
	return {"access_token": access_token, "token_type": "bearer"}

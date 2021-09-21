from os import access
from bookstore.models.user import UserModel
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from bookstore.repository.user import UserRepository
from bookstore.schemas.user import UserSchemaResponse, Login, Settings
from db import get_db
from ..hashing import Hash

user_login_router = APIRouter(tags=['Authenticate'])

get_db = get_db

@AuthJWT.load_config
def get_config():
	return Settings()


@user_login_router.post('/login', status_code=status.HTTP_200_OK)
def login(request: Login, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
	user = db.query(UserModel).filter(UserModel.username == request.username).first()

	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

	if not Hash.verify(user.password,request.password):
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")

	access_token = Authorize.create_access_token(subject=user.username)
	refresh_token = Authorize.create_refresh_token(subject=user.username)
	return {"access_token": access_token,"refresh_token": refresh_token, "token_type": "bearer"}

@user_login_router.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):
	Authorize.jwt_refresh_token_required()

	current_user = Authorize.get_jwt_subject()
	new_access_token = Authorize.create_access_token(subject=current_user)
	return {"access_token": new_access_token}
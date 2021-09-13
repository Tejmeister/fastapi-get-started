from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from bookstore.repository.user import UserRepository
from bookstore.schemas.user import UserSchemaCreate, UserSchemaFull, UserSchemaResponse
from db import get_db

user_router = APIRouter(prefix="/user", tags=['Users'])

get_db = get_db


@user_router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserSchemaResponse)
def create(request: UserSchemaCreate, db: Session = Depends(get_db)):
	return UserRepository(db).create(request)


@user_router.get('/{id}', status_code=200, response_model=UserSchemaResponse)
def get(id: int, db: Session = Depends(get_db)):
	return UserRepository(db).show(id)

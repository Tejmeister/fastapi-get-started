from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from bookstore.repository.item import ItemRepository
from bookstore.schemas.item import ItemSchemaCreate, ItemSchemaFull, ItemSchemaResponse
from bookstore.schemas.user import UserSchemaFull, UserSchemaCreate
from db import get_db
from ..oauth2 import get_current_user

item_router = APIRouter(prefix="/item", tags=['Item'])
items_router = APIRouter(prefix="/items", tags=['Items'])

get_db = get_db


@items_router.get("/", response_model=List[ItemSchemaResponse])
def get_all(db: Session = Depends(get_db), current_user: UserSchemaFull = Depends(get_current_user)):
	return ItemRepository(db).get_all()


@item_router.post('/', status_code=status.HTTP_201_CREATED, response_model=ItemSchemaFull)
def create(request: ItemSchemaCreate, db: Session = Depends(get_db), current_user: UserSchemaFull = Depends(get_current_user)):
	return ItemRepository(db).create(request)


@item_router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete(id: int, db: Session = Depends(get_db), current_user: UserSchemaFull = Depends(get_current_user)):
	return ItemRepository(db).delete(id)


@item_router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: ItemSchemaCreate, db: Session = Depends(get_db), current_user: UserSchemaFull = Depends(get_current_user)):
	return ItemRepository(db).update(id, request)


@item_router.get('/{id}', status_code=200, response_model=ItemSchemaFull)
def get(id: int, db: Session = Depends(get_db), current_user: UserSchemaFull = Depends(get_current_user)):
	return ItemRepository(db).get(id)

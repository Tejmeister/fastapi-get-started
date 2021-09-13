from sqlalchemy.orm import Session
from bookstore.models.user import UserModel
from bookstore.schemas.user import UserSchemaCreate
from fastapi import HTTPException, status
from ..hashing import Hash

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, request: UserSchemaCreate):
        new_user = UserModel(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def show(self, id: int):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with the id {id} is not available")
        return user

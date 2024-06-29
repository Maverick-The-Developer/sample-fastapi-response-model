from typing import List
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserInDB, UserListResponse
from sqlalchemy import func, select, insert


def create_user(db: Session, user: UserCreate) -> UserInDB | None:
    stmt = insert(User).values(
        email=user.email, password=user.password, name=user.name, role=user.role
    )
    result = db.execute(stmt)
    db.commit()

    user_id = result.inserted_primary_key[0]

    db_user = db.execute(select(User).filter(User.id == user_id)).scalar_one_or_none()

    if db_user is None:
        return None

    return UserInDB(
        id=db_user.id,
        email=db_user.email,
        name=db_user.name,
        role=db_user.role,
        password="",
    )


def get_user_list(db: Session) -> UserListResponse:
    userCount = db.execute(select(func.count(User.id))).scalar()
    userList = db.execute(select(User).order_by(User.id.desc())).scalars().all()
    users: List[UserInDB] = [
        UserInDB(
            id=user.id, email=user.email, name=user.name, role=user.role, password=""
        )
        for user in userList
    ]
    return UserListResponse(count=userCount, users=users)


def select_user(db: Session, user_id: int) -> UserInDB | None:
    return db.query(User).filter(User.id == user_id).one_or_none()

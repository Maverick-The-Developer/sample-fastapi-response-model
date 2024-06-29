from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from schemas import UserCreate, UserCreateResponse, UserInDB, UserListResponse
from services import create_user, get_user_list, select_user

user_router = APIRouter()


@user_router.post("", response_model=UserCreateResponse, status_code=201)
def post_user(postuser: UserCreate, db=Depends(get_db)):
    db_user = create_user(db, postuser)
    if db_user is None:
        return {"success": False, "message": "User Not Created", "user": None}
    return {"success": True, "message": "User Created", "user": db_user}


@user_router.get("", response_model=UserListResponse)
def get_users(db=Depends(get_db)):
    returnValue = get_user_list(db)
    return returnValue


@user_router.get("/{user_id}", response_model=UserInDB)
def get_user(user_id: int, db=Depends(get_db)):
    user = select_user(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=404, detail="고유번호에 해당하는 사용자가 없습니다."
        )
    return user

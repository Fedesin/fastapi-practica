# app/routes/users.py
from fastapi import APIRouter, HTTPException
from app.core.database import db
from app.models.user import User
from bson import ObjectId

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User)
async def create_user(user: User):
    user_dict = user.dict()
    result = await db["users"].insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    return user_dict

@router.get("/", response_model=list[User])
async def list_users():
    users = await db["users"].find().to_list(100)
    for u in users:
        u["id"] = str(u["_id"])
    return users

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = await db["users"].find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["id"] = str(user["_id"])
    return user

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from user_store import UserStore
import uuid

app = FastAPI()
store = UserStore("users.db")


class UserIn(BaseModel):
    name: str
    email: str


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None


@app.get("/users")
def get_users():
    return store.load()


@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = store.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user


@app.post("/users", status_code=201)
def create_user(user_in: UserIn):
    new_user = {
        "id": str(uuid.uuid4()),
        "name": user_in.name,
        "email": user_in.email,
    }
    store.save(new_user)
    return new_user


@app.put("/users/{user_id}")
def update_user(user_id: str, data: UserUpdate):
    updates = {k: v for k, v in data.model_dump().items() if v is not None}
    if not updates:
        raise HTTPException(status_code=400, detail="no fields to update")
    success = store.update_user(user_id, updates)
    if not success:
        raise HTTPException(status_code=404, detail="user not found")
    return store.find_by_id(user_id)


@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    success = store.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="user not found")
    return {"message": "user deleted"}

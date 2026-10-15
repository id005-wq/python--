from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "张三"}

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return {"message": "创建成功", "user": user}
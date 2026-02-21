from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    # Define que chave será 'message' e o valor, uma string
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]

from pydantic import BaseModel, Field

from utils.generator import UserDataGenerator


class User(BaseModel):
    first_name: str = Field(default_factory=UserDataGenerator.generate_first_name)
    last_name: str = Field(default_factory=UserDataGenerator.generate_last_name)


class UserRegistrationResponse(BaseModel):
    book: list
    userID: str
    username: str


class UserAccountPayload(BaseModel):
    userName: str = Field(default_factory=UserDataGenerator.generate_user_name)
    password: str = 'SomePassword!2021'  # Field(default_factory=lambda: UserDataGenerator.generate_password(length=20)) Закомменитл т.к багует


class UserAccount(UserAccountPayload):
    create_date: str = None
    expires: str = None
    isActive: bool = None
    token: str = None
    userId: str = None

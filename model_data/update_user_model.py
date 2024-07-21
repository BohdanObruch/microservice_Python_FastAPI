from pydantic import BaseModel


class UpdateUser(BaseModel):
    email: str
    first_name: str
    last_name: str
    avatar: str


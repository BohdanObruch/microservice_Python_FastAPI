from pydantic import BaseModel


class RegisterUser(BaseModel):
    email: str
    first_name: str

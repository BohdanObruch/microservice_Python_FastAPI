from pydantic import BaseModel


class UserData(BaseModel):
    name: str
    job: str

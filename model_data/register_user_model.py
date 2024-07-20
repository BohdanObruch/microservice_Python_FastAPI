from pydantic import BaseModel


class UnsuccessfulRegister(BaseModel):
    email: str

from pydantic import BaseModel
from typing import Optional


class EmployeeModel(BaseModel):
    firstname: str
    lastname: str
    email_address: str
    is_manager: Optional[bool] = False
    is_executive: Optional[bool] = False

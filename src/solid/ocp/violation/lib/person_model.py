from typing import Optional
from pydantic import BaseModel
from src.solid.ocp.violation.lib.employee_types import EmployeeType
from typing import Optional


class PersonModel(BaseModel):
    firstname: str = None
    lastname: str = None
    type_of_employee: Optional[EmployeeType] = EmployeeType.STAFF

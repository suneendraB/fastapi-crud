from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int
    email: str
    course: str


class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    model_config = {
        "from_attributes": True
    }


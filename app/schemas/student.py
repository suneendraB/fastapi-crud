from pydantic import BaseModel, EmailStr, Field

class StudentBase(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    course: str = Field(min_length=2)


class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    model_config = {
        "from_attributes": True
    }


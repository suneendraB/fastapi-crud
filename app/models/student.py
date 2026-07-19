from sqlalchemy import Column, Integer, String
from app.database import Base
#every ORM model inherits from Base

class Student(Base):
    __tablename__ = "students"
    # sql table - created in the name of students

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,unique=True, nullable=False)
    age = Column(Integer,nullable=False)
    course = Column(Integer,nullable=False)



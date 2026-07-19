from fastapi import APIRouter, HTTPException, Response,status
from app.schemas.student import Student
from app.services import student_service

router = APIRouter()

@router.get("/students")
def get_students():
    return student_service.get_all_students()

@router.get("/students/{student_id}")
def get_student(student_id: int):
    student = student_service.get_student_by_id(student_id)

    if student is None:
        raise HTTPException(status_code=404,detail="Student Not Found")

    return student

# {student_id} = path parameter
# student_id: int = validator - for same datatype

@router.post("/students")
def create_student_api(student: Student):
    return student_service.create_student(student.model_dump())

@router.put("/students/{student_id}")
def update_student_api(student_id: int, updated_student: Student):
    student = student_service.update_student(student_id,updated_student.model_dump())

    if student is None:
        raise HTTPException(status_code=404,detail="Student Not Found")

    return student

@router.delete("/students/{student_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def delete_student_api(student_id: int):
    deleted = student_service.delete_student(student_id)

    if not deleted:
        raise HTTPException(status_code=404,detail="Student Not Found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# router layer =  handles HTTP - request/response, status codes , exceptions

from fastapi import APIRouter, HTTPException, Response,status
from app.schemas.student import Student
from app.repositories import student_repositories
router = APIRouter()

@router.get("/students")
def get_students():
    return student_repositories.get_all_students()

@router.get("/students/{student_id}")
def get_student(student_id: int):
    student = student_repositories.get_student_by_id(student_id)

    if student is None:
        raise HTTPException(status_code=404,detail="Student Not Found")

    return student

# {student_id} = path parameter
# student_id: int = validator - for same datatype

@router.post("/students")
def create_student_api(student: Student):
    return student_repositories.create_student(student.model_dump())

@router.put("/students/{student_id}")
def update_student_api(student_id: int, updated_student: Student):
    student = student_repositories.update_student(student_id,updated_student.model_dump())

    if student is None:
        raise HTTPException(status_code=404,detail="Student Not Found")

    return student

@router.delete("/students/{student_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def delete_student_api(student_id: int):
    deleted = student_repositories.delete_student(student_id)

    if not deleted:
        raise HTTPException(status_code=404,detail="Student Not Found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# router layer =  handles HTTP - request/response, status codes , exceptions

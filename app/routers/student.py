from fastapi import APIRouter, HTTPException, Response,status, Depends
from sqlalchemy.orm import Session

from app.schemas.student import StudentCreate, StudentUpdate, StudentResponse
from app.services import student_service
from app.dependencies import get_db

router = APIRouter()

@router.get("/students",
            response_model=list[StudentResponse]
            )
def get_students(
        course: str | None = None,
        age: int | None = None,
        search: str | None = None,
        sort: str | None = None,
        page: int = 1,
        size: int = 5,
        db: Session = Depends(get_db)
):
    return student_service.get_all_students(
        db,
        course,
        age,
        search,
        sort,
        page,
        size
    )

@router.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(student_id: int,
                db: Session = Depends(get_db)
                ):
    student = student_service.get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(status_code=404,detail="Student Not Found")

    return student

# {student_id} = path parameter
# student_id: int = validator - for same datatype

@router.post("/students",
             response_model=StudentResponse,
             status_code=status.HTTP_201_CREATED
             )
def create_student_api(
        student: StudentCreate,
        db: Session = Depends(get_db)
):
    return student_service.create_student(
        db,
        student.model_dump()
    )

@router.put(
    "/students/{student_id}",
    response_model=StudentResponse
    )
def update_student_api(student_id: int,
                       updated_student: StudentUpdate,
                       db: Session = Depends(get_db)
                       ):
    student = student_service.update_student(
        db,
        student_id,
        updated_student.model_dump())

    if student is None:
        raise HTTPException(status_code=404,detail="Student Not Found")

    return student

@router.delete("/students/{student_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def delete_student_api(student_id: int, db: Session = Depends(get_db)):
    deleted = student_service.delete_student(db,student_id)

    if not deleted:
        raise HTTPException(status_code=404,detail="Student Not Found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# router layer =  handles HTTP - request/response, status codes , exceptions

from fastapi import APIRouter, HTTPException, Response,status
from app.schemas.student import Student
router = APIRouter()

students = [
    {
        "id":1,
        "name": "Rahul",
        "email": "rahul@gmail.com",
        "age" : 21,
        "course" : "Mechanical"
    },
    {
        "id": 2,
        "name": "Ravi",
        "email": "ravi@gmail.com",
        "age": 25,
        "course": "Robotics"
    },
    {
        "id":3,
        "name": "Suneendra",
        "age":28,
        "email":"suneendrabsa@gmail.com",
        "course":"Backend Engineering"
    }
]

@router.get("/students")
def get_students():
    # return {"message":"All students"}
    return students

@router.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404,detail="Student Not Found")

# {student_id} = path parameter
# student_id: int = validator - for same datatype

@router.post("/students")
def create_student(student: Student):
    new_student = student.model_dump()
    new_student["id"] = len(students) + 1
    students.append(new_student)

    return new_student


@router.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for student in students:
        if student["id"] == student_id:
            student.update(updated_student.model_dump())
            return student
    raise HTTPException(status_code=404,detail="Student Not Found")


@router.delete("/students/{student_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404,detail="Student Not Found")




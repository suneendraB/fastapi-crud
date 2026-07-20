from sqlalchemy.orm import Session
from app.models.student import Student
from sqlalchemy import desc

def get_all_students(db: Session,
                     course: str | None = None,
                     age: int | None = None,
                     search: str | None = None,
                     sort: str | None = None,
                     page: int = 1,
                     size: int = 5
                     ):
    query = db.query(Student)

    # Filtering

    if course:
        query = query.filter(Student.course == course)

    if age is not None:
        query = query.filter(Student.age == age)

    # searching
    if search:
        query = query.filter(
            Student.name.ilike(f"%{search}%")
                             )

    #sorting
    if sort == "age":
        query = query.order_by(Student.age)

    elif sort == "-age":
        query = query.order_by(desc(Student.age))

    # Pagination

    offset = (page - 1 ) * size

    query = query.offset(offset).limit(size)

    return query.all()

def get_student_by_id(db:Session, student_id: int):
    return (
        db.query(Student)
        .filter(Student.id == student_id)
        .first())

def create_student(db: Session, student_data: dict):
    db_student = Student(**student_data)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db:Session, student_id: int, updated_data: dict):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student:

        for key, value in updated_data.items():
            setattr(student, key, value)

        db.commit()

        db.refresh(student)

    return student


def delete_student(db,student_id: int):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student:
        db.delete(student)
        db.commit()

    return student is not None


# repository layer  = data access = - find / create/ update/ delete
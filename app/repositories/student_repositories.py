from sqlalchemy.orm import Session
from app.models.student import Student

def get_all_students(db: Session):
    return db.query(Student).all()

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
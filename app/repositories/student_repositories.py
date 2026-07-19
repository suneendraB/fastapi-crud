from app.database import SessionLocal
from app.models.student import Student

def get_all_students():

    db = SessionLocal()

    students = db.query(Student).all()

    db.close()

    return students

def get_student_by_id(student_id: int):

    db = SessionLocal()

    student = db.query(Student).filter(Student.id == student_id).first()

    db.close()

    return student

def create_student(student_data: dict):
    db = SessionLocal()

    db_student = Student(**student_data)

    db.add(db_student)

    db.commit()

    db.refresh(db_student)

    db.close()

    return db_student


def update_student(student_id: int, updated_data: dict):

    db = SessionLocal()

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

    db.close()

    return student


def delete_student(student_id: int):

    db = SessionLocal()

    student = (db.query(Student).filter(Student.id == student_id).first())

    if student:
        db.delete(student)
        db.commit()

    db.close()

    return student is not None


# repository layer  = data access = - find / create/ update/ delete